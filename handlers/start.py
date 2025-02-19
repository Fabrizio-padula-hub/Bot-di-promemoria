from telegram import Update
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Ciao! Sono il tuo bot di promemoria. Usa il comando /remind <tempo> <messaggio> per impostare un promemoria.\n"
        "Esempio: /remind 5m Comprare il latte"
    )