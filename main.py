from fastapi import FastAPI
from db import database, models
from routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(database.engine)

@app.get("/", tags=['Main Root'])
def root():
    return {"message": "Wellcome to blog api"}

app.include_router(blog.router)
app.include_router(user.router)