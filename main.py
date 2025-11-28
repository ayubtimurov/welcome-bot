from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8563593507:AAH08Fg8DBUy5tBup8MYqPhwso-aAlVbWv4'
BOT_USERNAME: Final = '@welcomeDIIbot'

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Start command recieved.")
    user = update.effective_user
    await update.message.reply_text(f"👋 Hello {user.first_name}. Welcome to Welcome Bot😊")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Help command recieved.")
    help_text = """
    🤖 *Bot Commands:*

/start - Start the bot and get welcome message
/help - Show this help message
"""
    await update.message.reply_text(help_text)



if __name__ == "__main__":
    print("Starting...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling(poll_interval=1)