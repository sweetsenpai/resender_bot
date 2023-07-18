from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from commands import start, resender, ban_user
import os
from server.ngrok_server import get_https
import logging


token = '6316622089:AAH7veU0phCyJcrOEqV7rZfmD2g9EOiFmX4'
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


PORT = int(os.environ.get('PORT', '70'))


def main() -> None:
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT | filters.PHOTO | filters.VIDEO, resender))
    application.add_handler(CallbackQueryHandler(ban_user))
    application.run_polling()
    # application.run_webhook(port=PORT, url_path=token, webhook_url=f'{get_https()}/{token}',
    #                         listen="0.0.0.0")


if __name__ == '__main__':
    main()
