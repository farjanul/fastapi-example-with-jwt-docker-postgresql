import random
import uuid
from datetime import datetime
import enum

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, Enum, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db import Base


class UserRole(enum.Enum):
    regular = "regular"
    staff = "staff"
    super_admin = "super_admin"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(String, default=str(random.randint(100000, 999999)))
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.regular)

    posts = relationship("Post", back_populates="user")



