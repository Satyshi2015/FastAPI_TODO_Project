from fastapi import FastAPI
from models import todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

#get all todo
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#get single todo

@app.get("/todos/{todo_id}")
async def get_todos(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return {"todo":todo}
    return {"message":"no todos found"}




#create a todo

@app.post("/todos")
async def create_todos(todo:todo):
    todos.append(todo)
    return {"message": "todos has been added"}


#update a todo

@app.put("/todos/{todo_id}")
async def update_todos(todo_id:int,todo_obj:todo):
    for todo in todos:
        if todo.id==todo_id:
            todo.id=todo_id
            todo.item=todo_obj.item
            return {"todo":todo}
    
    return {"message": "no todos has been updated"}

#delete a todo

@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            todos.remove(todo)
            return {"message":"todo has been deleted"}
    return {"message":"no todos found to delete"}


