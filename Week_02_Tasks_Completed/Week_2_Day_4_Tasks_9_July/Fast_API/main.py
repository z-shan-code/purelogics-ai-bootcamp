from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="To-Do List API")

# ---------- In-memory storage ----------
todos = []
next_id = 1  # simple counter to auto-generate IDs


# ---------- Pydantic Models ----------
class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


# ---------- Question 1: Create a task ----------
@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "completed": False
    }
    todos.append(new_todo)
    next_id += 1
    return new_todo


# ---------- Question 2: Get all tasks ----------
@app.get("/todos", response_model=list[Todo])
def get_all_todos():
    return todos


# ---------- Question 3: Get a specific task by ID ----------
@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Task not found")


# ---------- Question 4: Update a task ----------
@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            if updated_todo.title is not None:
                todo["title"] = updated_todo.title
            if updated_todo.completed is not None:
                todo["completed"] = updated_todo.completed
            return todo
    raise HTTPException(status_code=404, detail="Task not found")


# ---------- Question 5: Delete a task ----------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": f"Task with id {todo_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")