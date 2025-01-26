from typing import List
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class Blog(Blog):
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
    blogs: List[Blog] = []
    class Config():
        orm_mode = True
        
# Response Model
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True