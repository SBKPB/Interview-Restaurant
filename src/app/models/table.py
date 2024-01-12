from typing import Optional

from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class RestaurantTableBase(SQLModel):
    max_people: int
    booker_id: Optional[UUID] = Field(default=None, foreign_key="user.id")
    booking_id: Optional[UUID] = Field(default=None, foreign_key="booking.id")


class RestaurantTableCreate(RestaurantTableBase):
    pass


class RestaurantTable(RestaurantTableBase, table=True):
    id: UUID = Field(default=uuid4(), primary_key=True)
