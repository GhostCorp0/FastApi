from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from standard_architecture.src.utils.db import get_db
from standard_architecture.src.user.dtos import UserSchema, UserResponseSchema
from standard_architecture.src.user import controller

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register",response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db:Session = Depends(get_db)):
    return controller.register(body,db)



