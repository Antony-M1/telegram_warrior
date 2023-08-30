# telegram_warrior

"Telegram Warrior" is a dynamic project designed to efficiently manage Telegram webhooks using the FastAPI framework. By seamlessly integrating FastAPI with Telegram's webhook capabilities, this project enables real-time notifications and messaging to Telegram groups. With a streamlined interface, users can effortlessly set up and manage webhooks while harnessing the power of FastAPI's asynchronous capabilities for optimal performance.

# Prerequisites
* [Python3.10+](https://www.python.org/downloads/release/python-3100/)
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

# Telegram Documentation
* [TDLib](https://github.com/Antony-M1/telegram_warrior/blob/main/docs/TDLib.md)
* [BotFather](https://github.com/Antony-M1/telegram_warrior/blob/main/docs/bot-father.md)
* [customwebhookbot.py](https://docs.python-telegram-bot.org/en/latest/examples.customwebhookbot.html)

### Send Message in Channel
* [sendDocument](https://core.telegram.org/bots/api#sendmessage)
* [send_message](https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.send_message)
* [🔥 Sample Code 🔥](https://github.com/Antony-M1/telegram_warrior/blob/main/docs/send-message-in-channel)

**YouTube**

* [How To Create A Telegram Bot Using Python? | Telegram Bot In Python Tutorial | Python | Simplilearn](https://www.youtube.com/watch?v=227uk4kDTM8)
* [How To Create A Telegram Bot In Python For Beginners (2023 Tutorial)](https://www.youtube.com/watch?v=vZtm1wuA2yc)

# Project Setup
* [Local Setup](https://github.com/Antony-M1/telegram_warrior/blob/main/docs/local_setup.md)

# Package List
* [FastAPI](https://fastapi.tiangolo.com/)
* [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
    * [Documentation]()