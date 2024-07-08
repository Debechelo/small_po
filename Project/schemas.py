from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

class UserBase(BaseModel):
    login: str
    password: str
    project_id: Optional[str] = None
    env: Optional[str] = None
    domain: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
    created_at: datetime
    locktime: Optional[datetime] 

    class Config:
        orm_mode = True

class Project(BaseModel):
    id: str
    name: str

class ProjectCreate(BaseModel):
    pass

class Lock(BaseModel):
    user_id: str