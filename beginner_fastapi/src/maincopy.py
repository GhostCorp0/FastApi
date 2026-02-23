from fastapi import FastAPI

from beginner_fastapi.models.base import Base
from beginner_fastapi.src.database import engine
from beginner_fastapi.routes import auth

app = FastAPI()
app.include_router(auth.router, prefix ="/auth")

Base.metadata.create_all(engine)