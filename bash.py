from telegram pip install python-telegram-bot import Update
from telegram.ext import python bot.py
 Updater, CommandHandler, CallbackContext
python bot.py

# Bot tokenini o'zgartiring
TOKEN = '7458508236:AAFVnY76V5DPO7xNoOr4nEIWzQxQU-gohFo'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom! Men sizga qushiq topishga yordam bera olaman.')

def search_song(update: Update, context: CallbackContext) -> None:
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text('Iltimos, qidirayotgan qushiq nomini kiriting.')
        return

    # Bu yerda qidirish logikasi bo'lishi kerak
    # Misol uchun, siz Spotify API yoki boshqa xizmatlardan foydalanishingiz mumkin.
    # Hozircha oddiy xabar yuboradi:
    update.message.reply_text(f'Qushiq uchun qidiruv: {query}')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search_song))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
