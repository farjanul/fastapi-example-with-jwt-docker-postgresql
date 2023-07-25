from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    featured_image = Column(String)
    user_id = Column(UUID, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    comments = relationship("Comment", back_populates="comments")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    comment = Column(String, index=True)
    user_id = Column(UUID, ForeignKey("users.id"))
    post = relationship("Post", back_populates="comments")
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
