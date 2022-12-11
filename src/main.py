from fastapi import FastAPI

from src.router import balance
from src.router import event
from src.router import reset

app = FastAPI()

@app.get("/balance")
async def get():
    return await balance.get()

@app.post("/event")
async def post():
    return await event.post()

@app.post("/reset")
async def post():
    return await reset.post()
