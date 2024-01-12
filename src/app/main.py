from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Query, HTTPException
from sqlmodel import select, Session

from typing import List

from app.db.db import get_session, init_db

from app.models import Ticket, TicketCreate, TicketRead, Booking

from uuid import uuid4


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/tickets/", response_model=List[TicketRead])
def read_tickets(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    tickets = session.exec(select(Ticket).offset(offset).limit(limit)).all()
    return tickets


@app.post("/tickets/", status_code=201)
async def create_ticket(ticket: TicketCreate, session: Session = Depends(get_session)):
    ticket = Ticket(id=uuid4(), title=ticket, price=150, expiry_date=ticket.expiry_date)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket


@app.get("/bookings/", response_model=List[TicketRead])
def read_tickets(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
):
    tickets = session.exec(select(Ticket).offset(offset).limit(limit)).all()
    return tickets


@app.post("/bookings/", status_code=201)
async def create_ticket(ticket: TicketCreate, session: Session = Depends(get_session)):
    ticket = Ticket(id=uuid4(), title=ticket, price=150, expiry_date=ticket.expiry_date)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket





