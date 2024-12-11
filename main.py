from fastapi import FastAPI, Depends
from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("BASE is cleared")
    await create_tables()
    print("BASE is ready for work")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)
