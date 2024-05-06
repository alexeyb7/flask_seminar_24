import datetime
from fastapi import FastAPI, HTTPException
import database as db
import models
from typing import List
from random import randint

app = FastAPI()


@app.get("/")
def root():
    return {"Message": "Hello"}


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = db.users.insert().values(name=f'user{i}', surname=f'surname{i}', email=f'mail{i}@mail.ru',
                                         password=f'qwerty{i}')
        await db.database.execute(query)
    return {'message': f'{count} fake users create'}


# read all users/

@app.get("/users/", response_model=List[models.UserRead])
async def read_users():
    query = db.users.select()
    return await db.database.fetch_all(query)


# read one user

@app.get("/users/{user_id}", response_model=models.UserRead)
async def read_user(user_id: int):
    query = db.users.select().where(db.users.c.id == user_id)
    user = await db.database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# update user

@app.put("/users/{user_id}", response_model=models.UserRead)
async def update_user(user_id: int, new_user: models.UserCreate):
    query = db.users.update().where(db.users.c.id == user_id).values(**new_user.dict())
    await db.database.execute(query)
    return {**new_user.dict(), "id": user_id}


# delete user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = db.users.delete().where(db.users.c.id == user_id)
    await db.database.execute(query)
    return {'message': 'User deleted'}

