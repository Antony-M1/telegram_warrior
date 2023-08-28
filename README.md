# telegram_warrior

"Telegram Warrior" is a dynamic project designed to efficiently manage Telegram webhooks using the FastAPI framework. By seamlessly integrating FastAPI with Telegram's webhook capabilities, this project enables real-time notifications and messaging to Telegram groups. With a streamlined interface, users can effortlessly set up and manage webhooks while harnessing the power of FastAPI's asynchronous capabilities for optimal performance.

# Prerequisites
* Python3.10+
* [MySQL 8+](https://github.com/Antony-M1/mysql_docker)

# Project Folder Structure
* [FastAPI](https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project)
* [FastAPI Official](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

Here we consider the `telegram_warrior` = `app` 

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

`or`

[Structure](https://stackoverflow.com/questions/64943693/what-are-the-best-practices-for-structuring-a-fastapi-project)
```
your_project
├── __init__.py
├── main.py
├── core
│   ├── models
│   │   ├── database.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── schema.py
│   └── settings.py
├── tests
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       └── test_v1.py
└── v1
    ├── api.py
    ├── endpoints
    │   ├── endpoint.py
    │   └── __init__.py
    └── __init__.py 
```

# Documentation
* [TDLib](https://github.com/Antony-M1/telegram_warrior/blob/main/docs/TDLib.md)
