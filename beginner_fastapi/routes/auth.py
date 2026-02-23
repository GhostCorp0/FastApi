import uuid

import bcrypt
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from beginner_fastapi.models.user import User
from beginner_fastapi.pydantic_schema.user_create import UserCreate
from fastapi import APIRouter

from beginner_fastapi.pydantic_schema.user_login import UserLogin
from beginner_fastapi.src.database import get_db

router= APIRouter()

@router.post('/signup',status_code = 201)
def signup_user(user:UserCreate,db:Session =Depends(get_db)):
    user_db =  db.query(User).filter(User.email ==  user.email).first()

    if user_db:
        raise HTTPException(400,'User with the same email already exists!')

    hashed_pw = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    user_db = User(id = str(uuid.uuid4()),email =user.email,name =user.name,password=hashed_pw)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@router.post('/login',status_code = 201)
def login_user(user:UserLogin,db:Session=Depends(get_db)):
     user_db = db.query(User).filter(User.email == user.email).first()
     if not user_db:
         raise HTTPException(400,'User  with this email does not exist!')

     is_match = bcrypt.checkpw(user.password.encode(),user_db.password)

     if not is_match:
         raise HTTPException(400,'Incorrect Password!')

     return user_db