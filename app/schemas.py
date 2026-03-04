from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class QuestionnaireCreate(BaseModel):
    title: str
    content: str

class ReferenceCreate(BaseModel):
    title: str
    content: str

class AnswerUpdate(BaseModel):
    answer: str
    citation: str | None = None