import telegram.error
from telegram.ext import ContextTypes
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from DB import session, Bans


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if session.query(Bans).filter(Bans.user_id == update.message.from_user.id).all():
        await update.message.reply_text(text='Вас забанил администратор, сожалею.')
        return
    msg = 'Здравствуйте! Отправьте мне Ваш пост, который Вы хотели бы разместить на канале Петроградской диаспоры. ' \
          'После проверки администраторами пост будет опубликован, либо отклонен. Благодарю за понимание!'
    await update.message.reply_text(text=msg)
    return


async def resender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/start':
        return start(update, context)

    if session.query(Bans).filter(Bans.user_id == update.message.from_user.id).all():
        await update.message.reply_text(text='Вас забанил администратор, сожалею.')
        return

    await context.bot.send_message(chat_id=352354383, text='Новое сообщение!')
    message = await context.bot.forward_message(chat_id=352354383, from_chat_id=update.message.chat_id,
                                                message_id=update.message.message_id)
    await context.bot.send_message(chat_id=352354383,
                                   text=f'Забанить пользователя @{message.chat.username} за спам?',
                                   reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Выдать бан🚫',
                                                                                            callback_data=f'BAN:{message.chat.id}')]]))
    try:
        await context.bot.send_message(chat_id=366585, text='Новое сообщение!')
        await context.bot.forward_message(chat_id=366585, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        await context.bot.send_message(chat_id=366585,
                                       text=f'Забанить пользователя @{message.chat.username} за спам?',
                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Выдать бан🚫',
                                                                                                callback_data=f'BAN:{message.chat.id}')]]))
    except telegram.error.BadRequest:
        pass
    await update.message.reply_text(text='Спасибо! Я отправил Ваш пост на модерацию.\n\nПрисоединяйтесь к ресурсам Петроградского района:\n'
                                         '\nЧат Диаспоры: @ChatPS\nМаркет: @PSideMarket\nПрофи и мастера: @PSPROF')


async def ban_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_ban = update.callback_query.data.replace('BAN:', '')
    session.add(Bans(user_id=int(user_ban)))
    session.commit()
    await update.callback_query.answer(text='Пользователь забанен', show_alert=True)
    return
