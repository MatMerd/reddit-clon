from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class PostBase(BaseModel):
    body: Optional[str] = None
    votes: Optional[int] = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


# Properties to receive via API on creation
class UserCreate(PostBase):
    body: str


# Properties to receive via API on update
class UserUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: Union[UUID, str]
    body: str
    ownner_id: Union[UUID, str] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Post(PostInDBBase):
    pass


# Additional properties stored in DB
class PostInDB(PostInDBBase):
    pass
