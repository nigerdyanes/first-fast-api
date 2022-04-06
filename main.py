from typing import List

from pydantic import BaseModel

from fastapi import FastAPI, Body, Path

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

app: FastAPI = FastAPI()

users: List[User] = []

@app.get("/user")
def index():
    return users

@app.get("/user/{user_id}")
def get_one(user_id: int = Path(...)):
    return user_id

@app.post("/user")
def create(user: User = Body(...)):
    users.append(user)
    return user