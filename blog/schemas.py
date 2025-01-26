from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    published: bool
    
# Response Model
class ShowBlog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True
    
# User Schema
class User(BaseModel):
    name: str
    email: str
    password: str
    
# Response Model for User
class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True