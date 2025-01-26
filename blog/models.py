from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Blog(Base):
    # Table name
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=False)