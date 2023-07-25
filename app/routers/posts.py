from uuid import UUID

from app.auth.authenticate import authenticate_user
from app.schemas import PostCreate
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Request
from fastapi_pagination import Page, paginate

from app.schemas.user import User
import app.schemas.post as post_schemas
from app.services import post as service
from app.settings import Settings

router = APIRouter(
    tags=["posts"],
    responses={404: {"Description": "Not found"}},
)


# Dependency
def get_db(request: Request):
    return request.state.db


@router.post("/posts/", response_model=dict, status_code=201)
def add_post(post_data: PostCreate, user: User = Depends(authenticate_user), db: Session = Depends(get_db)):
    service.create_user_item(db, post_data, user.id)
    return {"message": "Post added successfully"}


@router.get("/posts/", response_model=Page[post_schemas.Post])
def get_post(db: Session = Depends(get_db)):
    return paginate(service.get_items(db))


@router.get("/posts/{post_id}/", response_model=post_schemas.Post)
def get_post(post_id: UUID, db: Session = Depends(get_db)):
    return service.get_item(db, post_id)


@router.get("/posts/users/{user_id}/", response_model=Page[post_schemas.Post])
def get_post_by_user(user_id: UUID, db: Session = Depends(get_db)):
    return paginate(service.get_items_by_user(db=db, user_id=user_id))
