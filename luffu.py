
from pyrogram import Client, filters
from pyrogram.types import Message

# Create a new Pyrogram client
api_id = 20693296

api_hash = 2c662827e953e4b8f3ca2f8695694dce

bot_token = 6237491510:AAFiSFLCzra8-3Ma4T9fju-Zwhffg7cGeJQ

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Handler function for the /start command
@Client.on_message(filters.command("start"))
def start_command(client: Client, message: Message):
    # Reply to the user with a welcome message
    message.reply_text("Welcome to my bot! How can I assist you?")

# Start the bot
bot.run()
