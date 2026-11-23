
import os
import random
import logging

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from messages import STUDY_TIPS, MOTIVATIONS


# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")


# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# Main menu keyboard
MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["📖 Quran & Knowledge", "🌙 Daily Reminder"],
        ["ℹ️ Help", "🏠 Main Menu"]
    ],
    resize_keyboard=True
)


# Format and send an Islamic reminder
async def send_reminder(update, context, messages, edit=False):
    reminder = random.choice(messages)

    message = (
        f"✨ <b>{reminder['type']}</b>\n\n"
        f"<b>{reminder['arabic']}</b>\n\n"
        f"{reminder['english']}\n\n"
        f"📚 <i>{reminder['reference']}</i>"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🔄 Another Reminder",
                callback_data="another"
            )
        ]
    ])

    if edit:
        await update.callback_query.edit_message_text(
            text=message,
            reply_markup=keyboard,
            parse_mode="HTML"
        )
    else:
        await update.message.reply_text(
            text=message,
            reply_markup=keyboard,
            parse_mode="HTML"
        )


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "🌙 <b>Welcome to Iqra!</b>\n\n"
        "اقْرَأْ — Read!\n\n"
        "Discover guidance and wisdom from the Quran "
        "and authentic Hadith.\n\n"
        "Receive Arabic texts, English translations, "
        "and their references.\n\n"
        "May Allah guide us all toward beneficial knowledge. 🤲"
    )

    await update.message.reply_text(
        welcome_message,
        reply_markup=MAIN_MENU,
        parse_mode="HTML"
    )


# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        "📖 <b>How to use Iqra</b>\n\n"
        "/start - Open the main menu\n"
        "/help - Show available commands\n"
        "/tip - Get a Quran or Hadith about knowledge\n"
        "/motivate - Receive an Islamic reminder\n\n"
        "You can also use the buttons below."
    )

    await update.message.reply_text(
        help_message,
        reply_markup=MAIN_MENU,
        parse_mode="HTML"
    )


# /tip command
async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_reminder(update, context, STUDY_TIPS)


# /motivate command
async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_reminder(update, context, MOTIVATIONS)


# Handle the "Another Reminder" button
async def another_reminder(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    query = update.callback_query
    await query.answer()

    await send_reminder(
        update,
        context,
        STUDY_TIPS + MOTIVATIONS,
        edit=True
    )


# Handle main menu buttons
async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = update.message.text

    if text == "📖 Quran & Knowledge":
        await tip(update, context)

    elif text == "🌙 Daily Reminder":
        await motivate(update, context)

    elif text == "ℹ️ Help":
        await help_command(update, context)

    elif text == "🏠 Main Menu":
        await start(update, context)

    else:
        await update.message.reply_text(
            "Please choose an option from the menu below.",
            reply_markup=MAIN_MENU
        )


# Main function
def main():
    if not TOKEN:
        raise ValueError("TOKEN is missing. Please check your .env file.")

    app = Application.builder().token(TOKEN).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("tip", tip))
    app.add_handler(CommandHandler("motivate", motivate))

    # Register button handlers
    app.add_handler(CallbackQueryHandler(another_reminder, pattern="^another$"))

    # Register normal text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Iqra bot is starting...")

    app.run_polling()


if __name__ == "__main__":
    main()
