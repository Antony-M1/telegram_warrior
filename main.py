from fastapi import FastAPI
from fastapi import BackgroundTasks
from core.telegram_bot.service import start_command, help_command, custom_command, handle_message, error


from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final
from core.settings import TELEGRAM_BOT_USERNAME, TELEGRAM_BOT_TOKEN, TELEGRAM_POLLING_SECONDS

app = FastAPI()


@app.get('/')
def home():
    return 'ok'


async def send_notification(message: str):
    # Your notification logic here
    print(f"Sending notification: {message}")

@app.get('/start-telegram-bot')
def start_telegram_bot(background_tasks: BackgroundTasks):
    print('Starting telegram----------------')
    # background_tasks.add_task(start_telegram_service)
    print('End telegram----------------')
    return 'Started telegram'


if __name__ == 'main':
    print('Starting Bot....................')
    telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # commands
    telegram_app.add_handler(CommandHandler('start', start_command))
    telegram_app.add_handler(CommandHandler('help', help_command))
    telegram_app.add_handler(CommandHandler('custom', custom_command))
    
    
    # Messages
    telegram_app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    telegram_app.add_error_handler(error)
    
    # Check Every 3 Seconds for new messages
    print('Polling ...................')
    telegram_app.run_polling(poll_interval=TELEGRAM_POLLING_SECONDS)
