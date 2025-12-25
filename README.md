# To-Do App
A simple to-do list backend built with FastAPI and SQLite.  
It supports CRUD (Create, Read, Update, Delete) operations for tasks and includes a Dockerfile and Docker Compose setup.

## Requirements
- Python 3.12
- FastAPI + Uvicorn
- SQLite
- Docker + Docker Compose

## API Endpoints
- `GET /health` — service status
- `POST /tasks` — create a task
- `GET /tasks` — list all tasks
- `GET /tasks/{task_id}` — get a task by id
- `PATCH /tasks/{task_id}` — update a task (partial update)
- `DELETE /tasks/{task_id}` — delete a task
