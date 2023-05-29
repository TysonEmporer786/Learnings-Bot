
from pyrogram import Client, filters
from pyrogram.types import Message

# Create a new Pyrogram client
bot = Client("your_bot")

# Handler function for the /start command
@Client.on_message(filters.command("start"))
def start_command(client: Client, message: Message):
    # Reply to the user with a welcome message
    message.reply_text("Welcome to my bot! How can I assist you?")

# Start the bot
bot.run()
