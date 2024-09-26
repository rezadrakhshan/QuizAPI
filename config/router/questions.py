from fastapi import APIRouter, Depends
from db.database import get_db
from db import schemas
from db import models
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(tags=["Questions"])


@router.get("/", response_model=List[schemas.QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    questions = db.query(models.Question).all()
    return questions


@router.post("/questions/", response_model=schemas.QuestionResponse)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    db_question = models.Question(text=question.text, author=question.author)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
