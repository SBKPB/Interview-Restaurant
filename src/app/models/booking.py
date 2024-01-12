from datetime import datetime
from typing import ClassVar, List, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel


class BookingBase(SQLModel):
    price: int
    # tables: List["Table"] = Relationship(back_populates="table")  # noqa: F821
    people_number: int
    appointment_date: datetime
    is_approval: Optional[bool] = None
    reviewer_id: Optional[int] = None


class BookingCreate(BookingBase):
    is_approval: bool = False


class Booking(BookingBase, table=True):

    id: UUID = Field(default=uuid4(), primary_key=True)
    is_approval: bool


class BookingRead(BookingBase):
    id: UUID
