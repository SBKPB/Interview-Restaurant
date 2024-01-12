from fastapi import APIRouter
from api.v1.endpoints import users, tickets, tables, bookings

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tickets.router, prefix="/tickets", tags=["tickets"])
api_router.include_router(tables.router, prefix="/tables", tags=["tables"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])