# бот_2
import telebot
from telebot import types

def bot_start(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start', 'старт'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Создание игр')
        btn2 = types.KeyboardButton('Мобильные приложения')
        btn3 = types.KeyboardButton('Веб разработка')
        btn4 = types.KeyboardButton('Софт для ПК')
        btn5 = types.KeyboardButton('Обработка данных')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        send_mess = f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление тебя интересует?'
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

    @bot.message_handler(commands=['gb'])
    def open_gb(message):
        # разметка
        markup = types.InlineKeyboardMarkup(row_width=3)
        # кнопки site_1, site_2
        site_1 = types.InlineKeyboardButton('Перейти на сайт GB', url='https://gb.ru/')
        site_2 = types.InlineKeyboardButton('Перейти на страницу с ДЗ', url='https://gb.ru/lessons/286606/homework')
        site_3 = types.InlineKeyboardButton('Перейти на страницу с ДЗ', url='https://gb.ru/lessons/286606/homework')
        markup.add(site_1, site_2, row_width=2)
        markup.add(site_3, row_width=3)
        # markup.add(site_1, site_2, row_width=2)

        bot.send_message(message.chat.id, 'Хорошо', parse_mode='html', reply_markup=markup)

    @bot.message_handler(commands=['insta'])
    def open_insta(message):
        # разметка
        markup = types.InlineKeyboardMarkup()
        # кнопка site
        site = types.InlineKeyboardButton('Перейти в Инстаграм', url='https://www.instagramm.com')
        markup.add(site)
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='html', reply_markup=markup)

    @bot.message_handler(commands=['vc'])
    def open_vc(message):
        # разметка
        markup = types.InlineKeyboardMarkup()
        # кнопка site
        site = types.InlineKeyboardButton('Перейти в VC', url='https://vc.com')
        markup.add(site)
        bot.send_message(message.chat.id, 'Хорошо', parse_mode='html', reply_markup=markup)
        # удаление разметки кнопок
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Убрал', parse_mode='html', reply_markup=None)

        # bot.send_message(message.chat.id, 'Убрал', reply_markup=a)

    @bot.message_handler(content_types=['text'])
    def mess(message):
        get_message_bot = message.text.strip().lower()
        if get_message_bot == 'создание игр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Для ПК')
            btn2 = types.KeyboardButton('Для Web')
            btn3 = types.KeyboardButton('Для смартфона')
            markup.add(btn1, btn2, btn3)
            final_message = 'Выберите окончательное направление'
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton('Создание игр')
            btn2 = types.KeyboardButton('Мобильные приложения')
            btn3 = types.KeyboardButton('Веб разработка')
            btn4 = types.KeyboardButton('Софт для ПК')
            btn5 = types.KeyboardButton('Обработка данных')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            final_message = 'Нажми на кнопки ниже'
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


        # bot.send_message(message.chat.id, message)


    bot.polling(none_stop=True)