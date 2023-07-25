import os

import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext

from app.utils.utils import dict_to_object

security = HTTPBearer()

SECRET_KEY = os.environ.get('SECRET_KEY')  # Replace with your secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db(request: Request):
    return request.state.db


def authenticate_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user: dict = payload
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid authentication")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return dict_to_object(user)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
