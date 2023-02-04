# бот_6 с использование get_updates и send_message
# get_updates
# Используйте этот метод для получения входящих обновлений с помощью длительного опроса (вики). Возвращает массив объектов обновления.
# send_message
# Используйте этот метод для отправки текстовых сообщений. В случае успеха возвращается отправленное сообщение.
import telebot
import time
import json


def bot_start(TOKEN):

    def gen_inline_markup():
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row_width = 3
        button_3 = telebot.types.InlineKeyboardButton("Три", callback_data="3")
        button_4 = telebot.types.InlineKeyboardButton("Четыре", callback_data="4")
        button_5 = telebot.types.InlineKeyboardButton("Пять", callback_data="5")
        markup.add(button_3, button_4, button_5)
        return markup

    def gen_reply_markup():
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = telebot.types.KeyboardButton('Сообщения')
        btn2 = telebot.types.KeyboardButton('Отчёты')
        btn3 = telebot.types.KeyboardButton('Управление')
        btn4 = telebot.types.KeyboardButton('Помощь')
        markup.add(btn1, btn2, btn3, btn4)
        return markup

    bot = telebot.TeleBot(TOKEN)
    offset = 0
    messages = bot.get_updates(offset)
    offset = messages[-1].update_id
    print(f'Offset {offset}')
    bot.send_message(messages[-1].message.chat.id, 'Видно||Не видно||', parse_mode='MarkdownV2', reply_markup=gen_reply_markup())

    timeout = 0
    while True:
        time.sleep(2)
        messages = bot.get_updates(offset=offset, timeout=timeout)
        print(len(messages))
        print(messages[-1].update_id)
        if offset < messages[-1].update_id:
            offset = messages[-1].update_id  # Присваиваем ID последнего отправленного сообщения боту

            for message in messages:
                print(len(messages))
                print(message.update_id)
                bot.send_message(message.message.chat.id, f'{message.message.chat.id}')

                # print(message.message.chat.id)





    def get_updates(offset=0):
        pass

    # Для того, что бы отправлять сообщение от имени бота, существует метод sendMessage
    def send_message(chat_id, text):
        pass

    # проверка текста сообщения
    def check_message(chat_id, message):
        print(message)
        # print(message['message']['text'].lower())
        if message['message']['text'].lower() in ['привет', 'ку', 'hello']:
            send_message(chat_id, 'Привет :)')
        elif message['message']['text'].lower() in 'сайт':
            inline_keyboard(chat_id, 'Кнопка "Сайт"')
        else:
            reply_keyboard(chat_id, 'Моя твоя не понимает!')



    # =====================
    # Встроенная клавиатура
    # =====================
    # InlineKeyboardMarkup - Этот объект представляет собой встроенную клавиатуру, которая появляется рядом с отправленным сообщением.
    def inline_keyboard(chat_id, text):
        # массив строк кнопок, каждая из которых представлена массивом объектов InlineKeyboardButton
        InlineKeyboardButton_1 = {'text': 'Команда____________________1', 'callback_data': 'Команда_1'}
        InlineKeyboardButton_2 = {'text': 'Сайт____________________2', 'url': 'https://www.soccer.ru'}
        InlineKeyboardButton_3 = {'text': 'Сайт____________________3', 'url': 'https://www.mail.ru'}
        reply_markup = {'inline_keyboard': [
            [InlineKeyboardButton_1, InlineKeyboardButton_2, InlineKeyboardButton_3],
            [InlineKeyboardButton_1, InlineKeyboardButton_2, InlineKeyboardButton_3]]}
        # print(reply_markup)
        data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
        # requests.post(f'{URL}{TOKEN}/sendMessage', data=data)



    # ReplyKeyboardMarkup - Этот объект представляет собой настраиваемую клавиатуру с параметрами ответа
    def reply_keyboard(chat_id, text):
        # Этот объект представляет собой настраиваемую клавиатуру с вариантами ответа (подробности и примеры см. в разделе Введение в ботов).
        reply_markup = {"keyboard": [["Фото по url", "Сайт"], ["Привет"]], "resize_keyboard": True,
                        "one_time_keyboard": True}
        data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
        # requests.post(f'{URL}{TOKEN}/sendMessage', data=data)


    # URL = 'https://api.telegram.org/bot'
    #
    # update_id = get_updates()[-1]['update_id']  # Присваиваем ID последнего отправленного сообщения боту
    # print(f'ID последнего сообщения {update_id}')
    # while True:
    #     time.sleep(2)
    #     messages = get_updates(update_id)  # Получаем обновления
    #     # print(len(messages))
    #     for message in messages:
    #         # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
    #         if update_id < message['update_id']:
    #             update_id = message['update_id']  # Присваиваем ID последнего отправленного сообщения боту
    #             # print(f"ID нового сообщения {message['update_id']}")
    #             print(message)
    #             if 'message' in message:
    #                 chat_id = message['message']['chat']['id']
    #                 # print(f"Чат ID {chat_id}")
    #                 # print(message)
    #                 check_message(chat_id, message)
    #             elif 'callback_query' in message:
    #                 callback_query_data = message['callback_query']['data']
    #                 print(callback_query_data)
    #                 # сообщение на нажатие кнопки
    #                 data = {'callback_query_id': message['callback_query']['id'],
    #                         'text': f'Ты нажал кнопку с командой {message["callback_query"]["data"]}'}
    #                 # requests.get(f'{URL}{TOKEN}/answerCallbackQuery', data=data)
    #                 time.sleep(1)
    #
    #                 # скрыть клавиатуру после нажатия
    #                 data = {'chat_id': message['callback_query']['message']['chat']['id'],
    #                         'message_id': message['callback_query']['message']['message_id']}
    #
    #                 # requests.post(f'{URL}{TOKEN}/editMessageReplyMarkup', data=data)
    #
    #                 InlineKeyboardButton_1 = {'text': 'Сайт_1', 'callback_data': 'Команда_2'}
    #                 InlineKeyboardButton_2 = {'text': 'Сайт_2', 'url': 'https://www.mail.ru'}
    #                 reply_markup = {'inline_keyboard': [[InlineKeyboardButton_1, InlineKeyboardButton_2]]}
    #                 # print(reply_markup)
    #                 data = {'chat_id': message['callback_query']['message']['chat']['id'], 'text': callback_query_data, 'reply_markup': json.dumps(reply_markup)}
    #                 # requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

