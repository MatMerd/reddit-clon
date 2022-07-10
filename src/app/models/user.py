from typing import TYPE_CHECKING
import uuid

from sqlalchemy import Boolean, Column, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_model import Base


if TYPE_CHECKING:
    from .post import Post  # noqa: F401
    from .comment import Comment  # noqa: F401


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nick_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    karma = Column(Float, default=0.0, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    posts = relationship("Post", back_populates="owner")
    comments = relationship("Comments", back_populates="owner")
