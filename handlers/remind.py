from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime, timedelta
import asyncio
from utils.time_parser import parse_time
from utils.reminders import send_reminder

async def remind(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 2:
        await update.message.reply_text("Per favore, usa il formato corretto: /remind <tempo> <messaggio>\n"
        "Esempio: /remind 5m Comprare il latte")
        return
    
    # Estrae il tempo e il messaggio
    time_str = context.args[0]
    reminder_message = ' '.join(context.args[1:])
    
    try:
        # Converte il tempo in un oggetto timedelta
        reminder_time = parse_time(time_str)
        if reminder_time is None:
            await update.message.reply_text("Formato tempo non valido. Usa formati come '5m', '2h', '1d'.")
            return
        
        # Calcola il tempo quando il promemoria verrà inviato
        reminder_time = datetime.now() + reminder_time
        
        # Invia subito il messaggio di conferma
        await update.message.reply_text(f"Promemoria impostato per {reminder_time.strftime('%H:%M:%S')}!")

        # Ora avvia il promemoria in background
        await send_reminder(update, reminder_time, reminder_message, context.bot)

    except Exception as e:
        await update.message.reply_text(f"Errore: {e}")