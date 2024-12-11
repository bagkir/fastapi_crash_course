from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import STaskAdd, STask, STaskId
from repository import TasksRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TasksRepository.find_all("task_id")
    return {"data": tasks}
