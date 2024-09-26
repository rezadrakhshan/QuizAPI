from .database import Base
from sqlalchemy.types import String, Integer, Boolean
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship


class Question(Base):
    __tablename__ = "Questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    author = Column(String)

    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "Answers"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    question_id = Column(Integer, ForeignKey("Questions.id"))
    question = relationship("Question", back_populates="answers")
    is_true = Column(Boolean, default=False)
