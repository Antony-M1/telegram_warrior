import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = bool(int(os.getenv('DEBUG')))

# Secret key
SECRET_KEY = os.getenv('SECRET_KEY')

# Telegram
TELEGRAM_BOT_NAME = os.getenv('TELEGRAM_BOT_NAME')
TELEGRAM_BOT_USERNAME = os.getenv('TELEGRAM_BOT_USERNAME')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_POLLING_SECONDS = int(os.getenv('TELEGRAM_POLLING_SECONDS'))
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


# Database
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
