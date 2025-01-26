from fastapi import FastAPI
from db import database, models
from routers import blog, user, auth
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


app = FastAPI()

models.Base.metadata.create_all(database.engine)

@app.get("/", tags=['Main Root'])
def root():
    return {"message": "Wellcome to blog api"}

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)