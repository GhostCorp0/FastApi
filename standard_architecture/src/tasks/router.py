from fastapi import APIRouter, Depends
from standard_architecture.src.tasks import controller
from standard_architecture.src.tasks.dtos import TaskSchema
from standard_architecture.src.utils.db import get_db

task_routes = APIRouter(prefix='/tasks')

@task_routes.post("/create")
def create_task(body:TaskSchema,db = Depends(get_db)):
    return controller.create_task(body,db)


