from uuid import UUID

from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException

from app import schemas
from app.auth.authenticate import pwd_context
from app.models.user import User, UserRole
from app.schemas.user import UserVerify


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session):
    return db.query(User).all()


def delete_user(db: Session, user_id: UUID):
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        db.delete(user)
        db.commit()
        db.close()
    return user


def verify_user(db: Session, user_data: UserVerify):
    user = get_user_by_email(db, user_data.email)
    if user.is_verified:
        raise HTTPException(status_code=400, detail="Account already verified")

    if user and user.verification_code == user_data.code:
        user.is_verified = True
        db.commit()
    else:
        raise HTTPException(status_code=400, detail="Wrong account or verification code.")
    return user


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    user = user.copy()
    user.password = hashed_password
    db_user = User(**user.dict())

    user_list = get_users(db)
    if not user_list:
        db_user.user_role = UserRole.super_admin

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


