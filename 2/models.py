# from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


# class BookStatus(Enum):
#     available = "available"
#     on_rental = "on_rental"


# class RequestStatus(Enum):
#     accepted = "accepted"
#     declined = "declined"


class Person(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=True)
    name: str
    age: Optional[int]
    profile_id: int | None = Field(foreign_key='profile.id')
    # Books: Optional[List['Book']]
    profile: Optional["Profile"] = Relationship(back_populates='profile_owner')


class Profile(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=True)
    nickname: str | None
    hobbies: str | None
    skills: str | None
    profile_owner: Optional["Person"] = Relationship(back_populates="profile")


# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     edition: int


# class BookOwnership(BaseModel):
#     book_id: int
#     person_id: int
#     status: BookStatus


# class Request(BaseModel):
#     id: int
#     sender_id: int
#     reciever_id: int
#     book_id: int
#     status: RequestStatus
