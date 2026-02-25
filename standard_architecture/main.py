from fastapi import  FastAPI

from standard_architecture.src.user.router import user_routes
from standard_architecture.src.utils.db import Base,engine
from standard_architecture.src.tasks.models import TaskModel
from standard_architecture.src.tasks.router import task_routes

Base.metadata.create_all(engine)
app = FastAPI(title = "This is my task management application")

app.include_router(task_routes)
app.include_router(user_routes)





