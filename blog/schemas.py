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