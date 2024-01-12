from typing import List, Optional
from uuid import UUID
from datetime import datetime
from sqlmodel import Field, SQLModel


class BookingBase(SQLModel):
    price: int
    tables: List[UUID]
    people_number: int
    appointment_date: datetime
    is_approval: Optional[bool] = None
    reviewer_id: Optional[UUID] = None

class BookingCreate(BookingBase):
    is_approval: bool = False


class Booking(BookingBase):
    id: UUID = Field(default=None, nullable=False, primary_key=True)
    is_approval: bool


