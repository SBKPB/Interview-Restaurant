import os
from sqlmodel import create_engine


DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True, future=True)