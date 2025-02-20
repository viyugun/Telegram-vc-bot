from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os

# Get the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your Telegram bot.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add a command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
