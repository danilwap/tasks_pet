from database import async_sessionmaker
from tasks_app.schemas import STaskAdd, STask, STaskId
from tasks_app.models import TaskOrm
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> STaskId:
        async with async_sessionmaker() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()

            return task.id



    @classmethod
    async def get_all(cls) -> list[STask]:
        async with (async_sessionmaker() as session):
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks