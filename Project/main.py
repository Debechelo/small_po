from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from typing import List
from database import SessionLocal, engine
import models, schemas, services
from sqlalchemy.dialects.postgresql import UUID

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User, summary="Создать пользователя", description="Создать нового пользователя.")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if not user.login or not user.password or not user.env or not user.domain:
        raise HTTPException(status_code=400, detail="Отсутствуют обязательные поля")
    
    existing_user = db.query(models.User).filter(models.User.login == user.login).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким логином уже существует")
    
    user_db = services.create_user(db, user)
    db.commit()
    
    return user_db

@app.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return services.get_users(db)

@app.post("/acquire-lock/", summary="Заблокировать пользователя", description="Заблокировать пользователя.")
def acquire_lock(lock: schemas.Lock, db: Session = Depends(get_db)):
    user_id = lock.user_id
    if not user_id:
        raise HTTPException(status_code=400, detail="Требуется указать идентификатор пользователя")
    
    if services.acquire_lock(db, user_id):
        return {"message": "Блокировка успешно применена"}
    else:
        raise HTTPException(status_code=400, detail="Пользователь уже заблокирован")

@app.post("/release-lock/", summary="Разблокировать пользователя", description="Разблокировать пользователя.")
def release_lock(lock: schemas.Lock, db: Session = Depends(get_db)):
    user_id = lock.user_id
    if not user_id:
        raise HTTPException(status_code=400, detail="Требуется указать идентификатор пользователя")
    
    if services.release_lock(db, user_id):
        return {"message": "Блокировка успешно снята"}
    else:
        raise HTTPException(status_code=400, detail="Пользователь не заблокирован")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


#######!!
@app.post("/projects/", response_model=schemas.Project, summary="Создать проект", description="Создать новый проект.")
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    if not project.name:
        raise HTTPException(status_code=400, detail="Требуется указать имя проекта")
    
    return services.create_project(db, project)
#######!!