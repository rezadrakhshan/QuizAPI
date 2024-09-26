from fastapi import FastAPI
from db import models
from db.database import engine
from router import questions, answers

app = FastAPI()

app.include_router(questions.router)
app.include_router(answers.router)

models.Base.metadata.create_all(bind=engine)
