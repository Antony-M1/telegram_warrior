from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from typing import Final
from core.settings import TELEGRAM_BOT_USERNAME, TELEGRAM_BOT_TOKEN



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Thangs for chating')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm Bannana! Please type something so I can respond")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


# Responses
def handle_response(text:str) -> str:
    
    processed: str = text.lower()
    print(f'Processed messgae  {processed}')
    if 'hello' in processed:
        return 'I am Good'
    
    if 'how are you' in processed:
        return 'I am good'
    
    if 'i love python' in processed:
        return 'Remember to subscribe!'

    return 'I am sorry, I do not understand'


async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User {update.message.chat.id} un {message_type}: {text}')
    
    if message_type == 'group':
        if TELEGRAM_BOT_USERNAME in text:
            new_text: str = text.replace(TELEGRAM_BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    print(f'Bot {response}')
    
    await update.message.reply_text(response)
    

async def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    

async def start_telegram_bot():
    print('Starting Bot....................')
    telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # commands
    telegram_app.add_handler(CommandHandler('start', start_command))
    telegram_app.add_handler(CommandHandler('help', help_command))
    telegram_app.add_handler(CommandHandler('start', custom_command))
    
    
    # Messages
    telegram_app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    telegram_app.add_error_handler(error)
    
    # Check Every 3 Seconds for new messages
    print('Polling ...................')
    telegram_app.run_polling(poll_interval=3)
