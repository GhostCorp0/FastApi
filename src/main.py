from fastapi import FastAPI, HTTPException

from models.base import Base
from src.database import engine
from routes import auth

app = FastAPI()
app.include_router(auth.router,prefix = "/auth")

Base.metadata.create_all(engine)