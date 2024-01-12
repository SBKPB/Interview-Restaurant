from sqlmodel import SQLModel

from app.models import Booking, RestaurantTable, Ticket, User  # noqa: F401

from .engine import engine


def init_db():
    SQLModel.metadata.create_all(engine)
