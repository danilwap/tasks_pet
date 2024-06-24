from fastapi import FastAPI, Depends
from tasks_app.schemas import STaskAdd, STask
from tasks_app.utils import create_db_and_tables
from typing import Annotated

from tasks_app.manager import TaskRepository
from tasks_app.router import router as tasks_app


async def lifespan(app: FastAPI):

    print('БД Запущена')

    await create_db_and_tables()
    yield


app = FastAPI(
    title='Task App',
    lifespan=lifespan
)

app.include_router(tasks_app)
