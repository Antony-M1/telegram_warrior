from fastapi import FastAPI
from fastapi import BackgroundTasks
from core.telegram_bot.service import start_telegram_service

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
    background_tasks.add_task(start_telegram_service)
    print('End telegram----------------')
    return 'Started telegram'
