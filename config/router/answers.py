from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from db import schemas, models

router = APIRouter(tags=["Answers"])


@router.post("/answers/", response_model=schemas.AnswerResponse)
def create_answer(answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    db_question = (
        db.query(models.Question)
        .filter(models.Question.id == answer.question_id)
        .first()
    )
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")

    db_answer = models.Answer(
        title=answer.title, question_id=answer.question_id, is_true=answer.is_true
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


@router.delete("/remove_answer/")
def remove_answer(answer: schemas.RemoveAnswer, db: Session = Depends(get_db)):
    try:
        db_answer = (
            db.query(models.Answer).filter(models.Answer.id == answer.id).first()
        )
        db.delete(db_answer)
        db.commit()
        return {"message": "Answer was delete"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Item not found")
