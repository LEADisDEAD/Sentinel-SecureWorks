from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from ..auth import get_current_user
import PyPDF2

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/reference/upload")
async def upload_reference(
    title: str = Form(None),
    content: str = Form(None),
    file: UploadFile = File(None),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Upload reference via raw text OR file (.txt, .pdf)
    """

    extracted_text = None

    # Case 1: Raw text input
    if content:
        extracted_text = content

    # Case 2: File upload
    elif file:
        if file.filename.endswith(".txt"):
            extracted_text = (await file.read()).decode("utf-8")

        elif file.filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file.file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            extracted_text = text

        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

    else:
        raise HTTPException(status_code=400, detail="Provide content or file")

    reference = models.ReferenceDocument(
        title=title if title else file.filename,
        content=extracted_text,
        user_id=current_user.id
    )

    db.add(reference)
    db.commit()

    return {"message": "Reference document uploaded successfully"}