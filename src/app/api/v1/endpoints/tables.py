from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import select

# from app.api.deps import CurrentUser, SessionDep
from app.models import Item, ItemCreate, ItemOut, ItemUpdate

router = APIRouter()