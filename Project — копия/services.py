from sqlalchemy.orm import Session
from models import User, Project
from schemas import UserCreate, ProjectCreate
from datetime import datetime
from passlib.context import CryptContext
import uuid

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        login=user.login,
        password=hashed_password,
        project_id=user.project_id,
        env=user.env,
        domain=user.domain,
        created_at=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_users(db: Session):
    return db.query(User).all()

def acquire_lock(db: Session, user_id: uuid.UUID):
    user = db.query(User).filter(User.id == user_id).first()
    if user.locktime:
        return False
    else:
        user.locktime = datetime.now()
        db.commit()
        return True

def release_lock(db: Session, user_id: uuid.UUID):
    user = db.query(User).filter(User.id == user_id).first()
    if user.locktime:
        user.locktime = None
        db.commit()
        return True
    else:
        return False
