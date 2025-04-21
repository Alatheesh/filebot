import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Get bot token and source channel ID from environment variables
TOKEN = os.environ.get('BOT_TOKEN')
SOURCE_CHANNEL_ID = os.environ.get('SOURCE_CHANNEL_ID')

if not TOKEN:
    logging.error("BOT_TOKEN environment variable not set!")
    exit(1)
if not SOURCE_CHANNEL_ID:
    logging.error("SOURCE_CHANNEL_ID environment variable not set!")
    exit(1)

try:
    SOURCE_CHANNEL_ID = int(SOURCE_CHANNEL_ID)
except ValueError:
    logging.error("Invalid SOURCE_CHANNEL_ID. It must be an integer.")
    exit(1)

async def start(update, context):
    await update.message.reply_text('Hello! Send me the name of a file to forward.')

async def forward_file(update, context):
    file_name = update.message.text
    bot = context.bot
    try:
        found = False
        async for message in bot.get_chat_history(chat_id=SOURCE_CHANNEL_ID):
            if message.document and message.document.file_name == file_name:
                await bot.copy_message(
                    chat_id=update.message.chat_id,
                    from_chat_id=SOURCE_CHANNEL_ID,
                    message_id=message.message_id
                )
                found = True
                break  # Stop searching after finding the file

        if not found:
            await update.message.reply_text(f"File '{file_name}' not found in the source channel.")

    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")
        logging.error(f"Error forwarding file: {e}")

async def main():
    application = Updater(TOKEN, use_context=True)

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_file))

    # Start the Bot
    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
