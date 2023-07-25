from uuid import UUID

from app.auth.authenticate import create_access_token, authenticate_user, pwd_context
import app.schemas as schemas
from fastapi.security import HTTPBasicCredentials
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, APIRouter, Request

from app.models.user import UserRole
from app.schemas.user import UserVerify
from app.services import user as service
from app.settings import Settings
from app.utils.email import send_verification_email

router = APIRouter(
    tags=["users"],
    responses={404: {"Description": "Not found"}},
)


# Dependency
def get_db(request: Request):
    return request.state.db


@router.post("/signup/", response_model=dict)
def sign_up(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    user = service.get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = service.get_user(db, user_data.username)
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = service.create_user(db, user_data)
    send_verification_email(user_data.email, new_user.verification_code)

    return {"message": "Sign-up successful. Please check your email for verification."}


@router.post("/login/", response_model=dict)
def login(credentials: HTTPBasicCredentials, db: Session = Depends(get_db)):
    user = service.get_user(db, credentials.username)

    if user is None or not pwd_context.verify(credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    elif user and not user.is_verified:
        raise HTTPException(status_code=403, detail="Please verify your email for an active account.")

    data = {
        "id": f'{user.id}',
        "username": credentials.username,
        "email": user.email,
        "user_role": user.user_role.value,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

    access_token = create_access_token(data=data)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/", response_model=Page[schemas.user.UserProfile])
def get_user_list(user: schemas.user.User = Depends(authenticate_user), db: Session = Depends(get_db)):
    if user.user_role == UserRole.regular.value:
        raise HTTPException(status_code=403, detail="You have no permission to perform this request.")

    return paginate(service.get_users(db))


@router.post("/users/verify/", response_model=dict)
def user_verify(user_data: UserVerify, db: Session = Depends(get_db)):
    service.verify_user(db, user_data)
    return {'message': 'User verified successfully'}


@router.delete("/users/{user_id}/", status_code=204)
def delete_user(user_id: UUID, user: schemas.user.User = Depends(authenticate_user), db: Session = Depends(get_db)):
    if user.user_role == UserRole.regular.value:
        raise HTTPException(status_code=403, detail="You have no permission to perform this request.")

    service.delete_user(db, user_id)


@router.get("/profile/", response_model=schemas.user.UserProfile)
def get_my_profile(user: schemas.user.User = Depends(authenticate_user), db: Session = Depends(get_db)):
    return service.get_user(db, username=user.username)

