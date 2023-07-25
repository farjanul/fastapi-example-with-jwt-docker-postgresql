from enum import Enum
from uuid import UUID

from pydantic import BaseModel, EmailStr

from app.schemas import Post


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class UserProfile(UserBase):
    id: UUID
    is_active: bool
    user_role: Enum
    is_verified: bool

    class Config:
        orm_mode = True


class User(UserBase):
    id: UUID
    is_active: bool
    user_role: Enum
    posts: list[Post] = []

    class Config:
        orm_mode = True


class UserVerify(BaseModel):
    email: EmailStr
    code: str

