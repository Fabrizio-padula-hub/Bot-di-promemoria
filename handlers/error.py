from telegram import Update
from telegram.ext import CallbackContext

def error(update: Update, context: CallbackContext) -> None:
    print(f"Error occurred: {context.error}")