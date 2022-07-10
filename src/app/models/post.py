from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_model import Base


if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .comment import Comment  # noqa: F401


class Post(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    body = Column(String, index=True, nullable=False)
    votes = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(Boolean(), default=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    owner = relationship("User", back_populates="posts")
    comments = relationship("Comments", back_populates="post")
