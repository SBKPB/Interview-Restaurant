from typing import Any, List
from uuid import uuid4

from fastapi import APIRouter, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models.booking import Booking, BookingCreate, BookingRead

router = APIRouter()


@router.get("/", response_model=List[BookingRead])
def read_tickets(
    *,
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> Any:
    bookings = session.exec(select(Booking).offset(offset).limit(limit)).all()
    return bookings


@router.post("/", status_code=201)
def create_ticket(booking: BookingCreate, session: SessionDep):
    booking = Booking(
        id=uuid4(),
        price=10000,
        people_number=booking.people_number,
        appointment_date=booking.appointment_date,
        is_approval=False,
    )
    session.add(booking)
    session.commit()
    session.refresh(booking)
    return booking
