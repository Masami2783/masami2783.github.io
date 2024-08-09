from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # URL вашего Web App
    web_app_url = "https://masami2783.github.io"

    # Создание кнопки, открывающей Web App
    keyboard = [
        [InlineKeyboardButton("Open Web App", web_app=web_app_url)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка сообщения с кнопкой
    await update.message.reply_text("Click the button below to open the Web App.", reply_markup=reply_markup)

def main() -> None:
    # Введите сюда токен вашего бота
    application = Application.builder().token("7284584129:AAFNm1mzoIV3OrJ0QmfJ3PoxPvV61TJe7pk").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == '__main__':
    main()
