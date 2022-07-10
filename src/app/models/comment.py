from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.orm import backref, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_model import Base


if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .post import Post  # noqa: F401


class Comment(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    body = Column(String, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(Boolean(), default=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    comments = relationship("Comments", backref=backref("parent_comment", remote_side="Comment.id"))
