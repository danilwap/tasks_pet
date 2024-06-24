from typing import Annotated, List

from fastapi import APIRouter, Depends

from tasks_app.manager import TaskRepository
from tasks_app.schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix='/tasks'
)


@router.post("/")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    res = await TaskRepository.add_one(task)
    return {'ok': True, "id": res}



@router.get('/')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
