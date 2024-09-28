from pydantic import BaseModel
from typing import List, Optional


class QuestionCreate(BaseModel):
    text: str
    author: str


class QuestionResponse(BaseModel):
    id: int
    text: str
    author: str
    answers: List["AnswerResponse"] = []

    class Config:
        orm_mode = True


class AnswerCreate(BaseModel):
    title: str
    question_id: int
    is_true: Optional[bool] = False


class AnswerResponse(BaseModel):
    id: int
    title: str
    is_true: bool
    question_id: int

    class Config:
        orm_mode = True


class RemoveQuestion(BaseModel):
    id :int


class RemoveAnswer(BaseModel):
    id : int