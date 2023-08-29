from fastapi import FastAPI
from core.telegram_bot.service import start_telegram_bot

app = FastAPI()

@app.route('/start-telegram-bot')
def start_telegram_bot():
    print('Starting telegram----------------')
    start_telegram_bot()
