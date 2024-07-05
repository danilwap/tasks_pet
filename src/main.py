from fastapi import FastAPI
from tasks_app.utils import create_db_and_tables
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
