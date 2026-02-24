from fastapi import  FastAPI
from standard_architecture.src.utils.db import Base,engine
from standard_architecture.src.tasks.models import TaskModel

Base.metadata.create_all(engine)
app = FastAPI(title = "This is my task management application")



