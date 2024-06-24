from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///tasks.db"

async_engine = create_async_engine(DATABASE_URL)
async_sessionmaker = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass