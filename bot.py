from telegram.ext import Application, CommandHandler
from handlers.start import start
from handlers.remind import remind
from handlers.error import error
from config import TOKEN

def main():
    # Crea l'Application con il token
    application = Application.builder().token(TOKEN).build()

    # Aggiungi i gestori dei comandi
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('remind', remind))

    # Aggiungi il gestore per gli errori
    application.add_error_handler(error)

    # Avvia il bot
    application.run_polling()

if __name__ == '__main__':
    main()