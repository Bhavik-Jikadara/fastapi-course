from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Blog Table
class Blog(Base):
    # Table name
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=False)

# User Table
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)