from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import select

# from app.api.deps import CurrentUser, SessionDep


router = APIRouter()
