from telegram.ext import CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton
from utils.text import texts, buttons
from utils.database_manager import language, get_chat
from utils.constants import MAIN_PAGE


def main_menu(update, context: CallbackContext):
    markup = [
        [KeyboardButton(buttons['order'][language(update)])],
        [KeyboardButton(buttons['watch_tutorial'][language(update)]),
         KeyboardButton(buttons['ask_question'][language(update)])],
        [KeyboardButton(buttons['change_language'][language(update)])]
    ]

    context.bot.send_message(chat_id=get_chat(update),
                             text=texts['main_menu'][language(update)],
                             reply_markup=ReplyKeyboardMarkup(markup, resize_keyboard=True))


def back_to_main(update, context):
    main_menu(update, context)
    return MAIN_PAGE
