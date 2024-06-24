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
    async def get_all(self) -> list[STask]:
        async with (async_sessionmaker() as session):
            query = select(TaskOrm)
            res = await session.execute(query)
            task_model = res.scalars().all()
            tasks = [STask.model_validate(task) for task in task_model]
            return tasks
