from typing import List, Optional
from uuid import UUID

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str
    telephone: str
    tickets: Optional[List[UUID]] = None
    bookings: Optional[List[UUID]] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: UUID = Field(default=None, nullable=False, primary_key=True)
    tickets: List[UUID] = Field(default=[])
    bookings: List[UUID] = Field(default=[])
    permissions: int = Field(default=1, nullable=False)


class AdministratorCreate(UserBase):
    pass


class Administrator(UserBase):
    permissions: int = Field(default=2, nullable=False)
