from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from datetime import datetime



class TicketBase(SQLModel):
    title: str
    price: float
    expiry_date: datetime

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: UUID = Field(default=uuid4(), primary_key=True)
    
class TicketRead(TicketBase):
    id: UUID




