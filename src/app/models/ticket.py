from sqlmodel import SQLModel, Field
from uuid import UUID
from datetime import datetime



class TicketBase(SQLModel):
    title: str
    price: float
    expiry_date: datetime

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: UUID = Field(default=None, nullable=False, primary_key=True)
    
class TicketRead(TicketBase):
    id: UUID




