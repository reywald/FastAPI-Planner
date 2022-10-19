from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "username": "FastPackt",
                "events": [],
            }
        }


class NewUser(User):
    pass


class UserSigIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }
