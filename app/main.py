from fastapi import FastAPI
from typing import List
from .task_update import UPDATE
from .task_create import CREATE
from .task_read import READ
from .task_delete import DELETE
from .task_managment import *

app = FastAPI(title="To Do App")

@app.on_event("startup")
def on_startup():
    init_database()

@app.post("/tasks", response_model=READ)
def api_create_task(payload: CREATE):
    return create_task(payload.title,payload.description,payload.starts,payload.due_date,payload.is_done,payload.level,payload.priority)


@app.get("/tasks", response_model=List[READ])
def api_list_tasks():
    return get_list_of_tasks()


@app.get("/tasks/{task_id}", response_model=READ)
def api_get_task(task_id: int):
    return get_task_by_id(task_id)


@app.patch("/tasks/{task_id}", response_model=READ)
def api_update_task(task_id: int, payload: UPDATE):
    return update_task(task_id,payload.title,payload.description,payload.starts,payload.due_date,payload.is_done,payload.level,payload.priority)


@app.delete("/tasks/{task_id}", response_model=DELETE)
def api_delete_task(task_id: int):
    delete_task(task_id)
    return {"deleted": True, "id": task_id}

@app.get("/health")
def health():
    return {"status": "ok"}
