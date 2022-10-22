from pydantic import BaseModel, EmailStr
from beanie import Document, Link
from typing import List, Optional
from .events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Setting:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }


class UserSigIn(User):
    email: EmailStr
    password: str
