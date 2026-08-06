from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    content: Optional[str] = None


class PostOut(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

