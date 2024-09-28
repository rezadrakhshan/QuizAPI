from fastapi import APIRouter, Depends, HTTPException
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


@router.delete("/remove_question/")
def remove_question(question: schemas.RemoveQuestion, db: Session = Depends(get_db)):
    try:
        db_question = (
            db.query(models.Question).filter(models.Question.id == question.id).first()
        )
        for i in db_question.answers:
            db_answers = db.query(models.Answer).filter(models.Answer.id == i.id).first()
            db.delete(db_answers)
            db.commit()
        db.delete(db_question)
        db.commit()
        return {"message": "Questions was delete"}
    except:
        raise HTTPException(status_code=404, detail="Question not found")
