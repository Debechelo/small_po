from sqlalchemy.orm import Session
from main import create_user, get_users, acquire_lock, release_lock

def test_create_user(db_session: Session):
    # Создание тестового пользователя
    user = {
        "login": "test_user",
        "password": "test_password",
        "project_id": "test_project",
        "env": "test_env",
        "domain": "test_domain"
    }
    
    created_user = create_user(db_session, user)
    
    # Проверка, что созданный пользователь существует в базе данных
    assert created_user is not None
    assert created_user.login == user["login"]
    assert created_user.project_id == user["project_id"]

def test_get_users(db_session: Session):
    # Получение всех пользователей
    users = get_users(db_session)
    
    # Проверка, что список пользователей не пустой
    assert len(users) > 0

def test_acquire_and_release_lock(db_session: Session):
    user = create_user(db_session, {
        "login": "test_user",
        "password": "test_password",
        "project_id": "test_project",
        "env": "test_env",
        "domain": "test_domain"
    })
    
    # Проверка, что пользователь не заблокирован
    assert acquire_lock(db_session, user.id)
    
    # Проверка, что пользователь заблокирован
    assert not acquire_lock(db_session, user.id)
    
    # Проверка, что блокировка успешно снята
    assert release_lock(db_session, user.id)
    
    # Проверка, что пользователь не заблокирован после снятия блокировки
    assert not release_lock(db_session, user.id)
