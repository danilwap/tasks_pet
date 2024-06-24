
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

from typing import Optional


class TaskOrm(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
