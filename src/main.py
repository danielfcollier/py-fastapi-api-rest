from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse

from src.router import *
from src.model import Event

app = FastAPI()

@app.get("/balance", status_code = status.HTTP_200_OK)
async def get(account_id: str):
    try:
        result = balance.get(account_id)
        print(result)
        if result is None:
            raise Exception()

        return result["balance"]

    except:
        return PlainTextResponse("0", status_code = status.HTTP_404_NOT_FOUND)

@app.post("/event", status_code = status.HTTP_201_CREATED)
async def post(request: Event.Request):
    try:
        result = event.post(request)
        if result is None:
            raise Exception()

        return result

    except:
        return PlainTextResponse("0", status_code = status.HTTP_404_NOT_FOUND)

@app.post("/reset", status_code = status.HTTP_200_OK)
async def post():
    try:
        result = reset.post()
        return PlainTextResponse(result)

    except:
        return PlainTextResponse("Bad Request", status_code = status.HTTP_400_BAD_REQUEST)
