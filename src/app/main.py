from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
