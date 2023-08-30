# Message in Channel

Here the sample code to help to send message in a channel
```
import asyncio
from telegram import Bot

async def send_message_to_channel():
    # Your bot's API token
    API_TOKEN = 'YOUR_BOT_API_TOKEN'
    
    # Initialize the bot
    bot = Bot(token=API_TOKEN)
    
    # The chat ID of the channel you want to send the message to
    channel_chat_id = '@your_channel_username'
    
    # The message you want to send
    message_text = 'Hello from your bot!'
    
    # Send the message to the channel
    await bot.send_message(chat_id=channel_chat_id, text=message_text)

# Run the async function using asyncio
asyncio.run(send_message_to_channel())

```