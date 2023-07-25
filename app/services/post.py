from uuid import UUID

from sqlalchemy.orm import Session

from app import schemas
from app.models.post import Post


def get_items(db: Session):
    return db.query(Post).filter(Post.is_active == True).all()


def get_item(db: Session, item_id: UUID):
    return db.query(Post).filter(Post.id == item_id).first()


def get_items_by_user(db: Session, user_id: UUID):
    return db.query(Post).filter(Post.user_id == user_id).all()


def create_user_item(db: Session, item: schemas.PostCreate, user_id: UUID):
    db_item = Post(**item.dict(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
