# бот_5 с помощью requests и API telegram
import telebot
import requests
import time
import json


# Telegram API входящие сообщения
# Для того что бы получить входящие обновления бота, воспользуемся методом getUpdates.
# получить сообщения от пользователя
# https://api.telegram.org/bot<ваш_токен>/getUpdates
# отправить сообщение от бота
# https://api.telegram.org/bot<ваш_токен>/sendMessage?chat_id=<ваш_chat_id>&text=Привет, хорошо, а ты как?

# Making requests
# All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form:
# https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example:
# https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe


def bot_start(TOKEN):
    # получить новые сообщения (список словарей)
    # offset - идентификатор первого возвращаемого обновления. Должен быть на единицу больше, чем самый высокий среди идентификаторов ранее полученных обновлений.
    # По умолчанию возвращаются обновления, начиная с самого раннего неподтвержденного обновления.
    # Обновление считается подтвержденным, как только вызывается getUpdates со смещением выше, чем его update_id.
    # Можно указать отрицательное смещение для получения обновлений, начиная с -offset update с конца очереди обновлений. Все предыдущие обновления будут забыты.
    def get_updates(offset=0):
        # получаем словарь в json формате
        result = requests.get(f'{URL}{TOKEN}/getUpdates?offset={offset}').json()
        # print(f"Сообщение {result['result']}")
        return result['result']

    # Для того, что бы отправлять сообщение от имени бота, существует метод sendMessage
    def send_message(chat_id, text):
        requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

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
        requests.post(f'{URL}{TOKEN}/sendMessage', data=data)
        # time.sleep(1)
        # editMessageReplyMarkup = {}
        # data = {'chat_id': chat_id, 'text': 'Убрал клаву', 'editMessageReplyMarkup': editMessageReplyMarkup}

        #         bot.edit_message_reply_markup(message.message.chat.id, message.message.message_id)
        # requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

    # ReplyKeyboardMarkup - Этот объект представляет собой настраиваемую клавиатуру с параметрами ответа
    def reply_keyboard(chat_id, text):
        # Этот объект представляет собой настраиваемую клавиатуру с вариантами ответа (подробности и примеры см. в разделе Введение в ботов).
        reply_markup = {"keyboard": [["Фото по url", "Сайт"], ["Привет"]], "resize_keyboard": True,
                        "one_time_keyboard": True}
        data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
        requests.post(f'{URL}{TOKEN}/sendMessage', data=data)

    URL = 'https://api.telegram.org/bot'
    # bot = telebot.TeleBot(TOKEN)

    update_id = get_updates()[-1]['update_id']  # Присваиваем ID последнего отправленного сообщения боту
    print(f'ID последнего сообщения {update_id}')
    while True:
        time.sleep(2)
        messages = get_updates(update_id)  # Получаем обновления
        # print(len(messages))
        for message in messages:
            # Если в обновлении есть ID больше чем ID последнего сообщения, значит пришло новое сообщение
            if update_id < message['update_id']:
                update_id = message['update_id']  # Присваиваем ID последнего отправленного сообщения боту
                # print(f"ID нового сообщения {message['update_id']}")
                print(message)
                if 'message' in message:
                    chat_id = message['message']['chat']['id']
                    # print(f"Чат ID {chat_id}")
                    # print(message)
                    check_message(chat_id, message)
                elif 'callback_query' in message:
                    callback_query_data = message['callback_query']['data']
                    print(callback_query_data)
                    # сообщение на нажатие кнопки
                    data = {'callback_query_id': message['callback_query']['id'],
                            'text': f'Ты нажал кнопку с командой {message["callback_query"]["data"]}'}
                    requests.get(f'{URL}{TOKEN}/answerCallbackQuery', data=data)
                    time.sleep(1)

                    # chat_id = message['callback_query']['message']['chat']['id']
                    # print(chat_id)
                    # message_id = message['callback_query']['message']['message_id']
                    # print(message_id)

                    data = {'chat_id': message['callback_query']['message']['chat']['id'],
                            'message_id': message['callback_query']['message']['message_id']}

                    response = requests.post(f'{URL}{TOKEN}/editMessageReplyMarkup', data=data)
                    InlineKeyboardButton_1 = {'text': 'Сайт_1', 'url': 'https://www.soccer.ru'}
                    InlineKeyboardButton_2 = {'text': 'Сайт_2', 'url': 'https://www.mail.ru'}
                    reply_markup = {'inline_keyboard': [[InlineKeyboardButton_1, InlineKeyboardButton_2]]}
                    # print(reply_markup)
                    data = {'chat_id': message['callback_query']['message']['chat']['id'], 'text': callback_query_data, 'reply_markup': json.dumps(reply_markup)}
                    requests.post(f'{URL}{TOKEN}/sendMessage', data=data)
                    # print(response)
                    # print(f"ID пользователя: {message['message']['chat']['id']}, Сообщение: {message['message']['text']}")
