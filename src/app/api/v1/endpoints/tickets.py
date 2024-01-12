from typing import Any, List
from uuid import uuid4

from fastapi import APIRouter, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models.ticket import Ticket, TicketCreate, TicketRead

router = APIRouter()


@router.get("/", response_model=List[TicketRead])
def read_tickets(
    *,
    session: SessionDep,
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> Any:
    tickets = session.exec(select(Ticket).offset(offset).limit(limit)).all()
    return tickets


@router.post("/", status_code=201)
async def create_ticket(ticket: TicketCreate, session: SessionDep) -> Any:
    ticket = Ticket(id=uuid4(), title=ticket, price=150, expiry_date=ticket.expiry_date)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket
