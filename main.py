from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to FastAPI!"

@app.get("/data")
def data():
    return {
        "data": {
            "name": "Bhavik Jikadara",
            "Age": 24,
            "Gender": "Male"
        }
    }

# Blog Path and Query parameters
# @app.get("/blog")
# def blog_limit():
#     return {
#         "Blog": "Blogs list"
#     }
    
@app.get("/blog")
def blog_limit(limit: int=10, published: bool=True, sort: Optional[str]=None):
    # By default 10 blogs show
    if published:
        return {
            "Blog": f"{limit} published blogs from the database."
        }
    else:
        return {
            "Blog": f"{limit} blogs from the database."
        }
    
@app.get("/blog/unpublished")
def unpublished():
    return {
        "Unpublished Blog": [
            {"Blog 1": "This is Blog 1"},
            {"Blog 2": "This is Blog 2"}
        ]
    }
    
@app.get("/blog/{id}")    
def blog(id: int):
    # fetch blog with id = id
    return {
        f"Blog {id}": f"Here is blog {id}"
    }
    
@app.get("/blog/{id}/comments")
def comments(id: int):
    return {
        f"comments {id}": "This is Good."
    }