# utils/reminders.py
import asyncio
from datetime import datetime
import time

async def send_reminder(update, reminder_time, reminder_message, bot) -> None:
    time_to_wait = (reminder_time - datetime.now()).total_seconds()
    if time_to_wait > 0:
        await asyncio.sleep(time_to_wait) 

    # Ora invia il messaggio usando await per la coroutine
    await bot.send_message(chat_id=update.message.chat_id, text=f"⏰ Ecco il tuo promemoria: {reminder_message}")