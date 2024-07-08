## Запуск проекта
Перейдите в корневую директорию проекта.
Запустите проект с помощью команды:


`
docker-compose up --build
`

После успешного запуска проекта вы сможете обращаться к API по адресу http://localhost:8000/

## Запросы

1. Создание пользователя

`http://localhost:8000/users/`

    Метод: `POST`

    Путь: `/users/`

Тело запроса: JSON
```
{
    "login": "example@example.com",
    "password": "my_secure_password",
    "project_id": "",
    "env": "prod",
    "domain": "regular"
}
```

2. Список пользованелей

`http://localhost:8000/users/`

    Метод: `GET`

    Путь: `/users/`

3. Заблокировать пользователя

`http://localhost:8000/acquire-lock/`

    Метод: `POST`

    Путь: `/acquire-lock/`

Тело запроса: JSON

```
{
    "user_id": "b1ddccbf-61e2-4f9e-a3f5-ef1ca5c7267c"
}
```

4. Разблокировать пользователя

`http://localhost:8000/release-lock/`

    Метод: `POST`

    Путь: `/release-lock/`

Тело запроса: JSON

```
{
    "user_id": "b1ddccbf-61e2-4f9e-a3f5-ef1ca5c7267c"
}
```
