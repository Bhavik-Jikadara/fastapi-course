from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from db import schemas, models, database
from utils.hashing import Hash
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

# Creating user
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    hashed_password = Hash.bcrypt(request.password)

    new_user = models.User(
        name=request.name, email=request.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get User
@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    
    return user