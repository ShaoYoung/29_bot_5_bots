# бот_3
import telebot
from telebot import types

def bot_start(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    # создание разметки
    def gen_markup():
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3
        button_3 = types.InlineKeyboardButton("Три", callback_data="3")
        button_4 = types.InlineKeyboardButton("Четыре", callback_data="4")
        button_5 = types.InlineKeyboardButton("Пять", callback_data="5")
        markup.add(button_3, button_4, button_5)
        return markup

    # обработчик всех ответов. func - функция-фильтр
    @bot.callback_query_handler(func=lambda message: True)
    def callback_query(message):
        answer = ''
        # всплывающее окно после нажатия кнопки (отклик на нажатие кнопки), в чат не передаётся.
        bot.answer_callback_query(message.id, "Спасибо за честный ответ")
        # message.data - это callback_data в InlineKeyboardButton
        if message.data == "3":
            answer = 'Вы троечник'
        elif message.data == "4":
            answer = 'Вы хорошист'
        elif message.data == "5":
            answer = 'Вы отличник'
            # ответ в чат
        bot.send_message(message.message.chat.id, answer)
        # редактирование только разметки ответов сообщений. по умолчанию reply_markup=0
        bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id)

    @bot.message_handler(func=lambda message: True)
    def message_handler(message):
        # print(message)
        bot.send_message(message.chat.id, "Какая у вас средняя оценка?", reply_markup=gen_markup())

    bot.polling(none_stop=True)