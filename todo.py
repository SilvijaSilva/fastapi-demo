# a fastapi system for account managament

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Todo(BaseModel):
    id: int
    name: str
    description: str
    date: datetime

# type hint for a list of todos
todos:list[Todo] = []

@app.post("/todos/")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}

@app.get("/todos/")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    todos[:] = [todo for todo in todos if todo.id != todo_id]
    return {"message": "Todo deleted successfully"}

