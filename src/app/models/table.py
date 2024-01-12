from typing import Optional
from uuid import UUID

from sqlmodel import Field, SQLModel


class TableBase(SQLModel):
    max_people: int
    booker: Optional[UUID]


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: UUID = Field(default=None, nullable=False, primary_key=True)
