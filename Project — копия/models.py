import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime)
    login = Column(String)
    password = Column(String)
    project_id = Column(String, ForeignKey('projects.id'), nullable=True)  # Изменен тип данных на String
    env = Column(String)
    domain = Column(String)
    locktime = Column(DateTime)

    project = relationship("Project", back_populates="users", primaryjoin="User.project_id == Project.id")

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)

    users = relationship("User", back_populates="project", primaryjoin="Project.id == User.project_id")
