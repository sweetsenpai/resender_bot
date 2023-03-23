import telegram.error
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler,filters
from telegram import Update
import os
from server.ngrok_server import get_https
import logging
token = os.environ['rs_token']
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


PORT = int(os.environ.get('PORT', '70'))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = 'Привет, отправь мне сообщения и я передам кому надо 😎!'
    await update.message.reply_text(text=msg)
    return


async def resender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/start':
        return start(update, context)
    await context.bot.send_message(chat_id=352354383, text='Новое сообщение!!!!!!')
    await context.bot.forward_message(chat_id=352354383, from_chat_id=update.message.chat_id,
                                      message_id=update.message.message_id)
    try:
        await context.bot.send_message(chat_id=366585, text='Новое сообщение!!!!!!')
        await context.bot.forward_message(chat_id=366585, from_chat_id=update.message.chat_id,message_id=update.message.message_id)
    except telegram.error.BadRequest:
        pass
    await update.message.reply_text(text='Ваше сообщение отправлено👍\nЕсли хочешь отправить что-нибудь ещё, то просто напиши мне)')


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT, resender))
    # application.run_polling()
    application.run_webhook(port=PORT, url_path=token, webhook_url=f'{get_https()}/{token}',
                            listen="0.0.0.0")


if __name__ == '__main__':
    main()
