from uuid import UUID

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str
    featured_image: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: UUID
    is_active: bool
    user_id: UUID

    class Config:
        orm_mode = True
