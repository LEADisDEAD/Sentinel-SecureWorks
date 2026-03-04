from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models
from ..auth import get_current_user
from .. import schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/questionnaire/upload")
def upload_questionnaire(
    data: schemas.QuestionnaireCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    questionnaire = models.Questionnaire(
        title=data.title,
        user_id=current_user.id
    )

    db.add(questionnaire)
    db.commit()
    db.refresh(questionnaire)

    # Split questions by newline
    questions = [q.strip() for q in data.content.split("\n") if q.strip()]

    for q_text in questions:
        question = models.Question(
            text=q_text,
            questionnaire_id=questionnaire.id
        )
        db.add(question)

    db.commit()

    return {
        "message": "Questionnaire uploaded successfully",
        "total_questions": len(questions)
    }