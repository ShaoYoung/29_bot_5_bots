# бот_4 с помощью requests и API telegram
# import telebot
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
        # print(result['result'])
        return result['result']

    # Для того, что бы отправлять сообщение от имени бота, существует метод sendMessage
    def send_message(chat_id, text):
        requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

    # проверка текста сообщения
    def check_message(chat_id, message):
        if message.lower() in ['привет', 'ку', 'hello']:
            send_message(chat_id, 'Привет :)')
        elif message.lower() in 'сайт':
            inline_keyboard(chat_id, 'Кнопка "Сайт"')
        elif message.lower() in 'фото по url':
            # Отправить URL-адрес картинки (телеграм скачает его и отправит)
            send_photo_url(chat_id, 'https://ramziv.com/static/assets/img/home-bg.jpg')
        elif message.lower() in 'фото с компьютера':
            # Отправить файл с компьютера
            print('Фото с ПК')
            send_photo_file(chat_id, 'photo/Good_Job.png')
        elif message.lower() in 'фото с сервера телеграм':
            # Отправить id файла (файл уже хранится где-то на серверах Telegram)
            send_photo_file_id(chat_id,
                               'AgACAgIAAxkBAAMqYVGBbdbivL53IzKLfUKUClBnB0cAApy0MRtfMZBKHL0tNw9aITwBAAMCAAN4AAMhBA')
        else:
            reply_keyboard(chat_id, 'Моя твоя не понимает!')

    # ============================
    # Отправка файлов Telegram API
    # ============================
    # В Telegram API есть три способа отправки файлов, для демонстрации воспользуемся методом sendPhoto и добавим три функции для отправки фотографии.
    # Первая способ: Предоставить файл по URL, Telegram скачает и отправит его (максимальный размер 5 МБ).
    def send_photo_url(chat_id, img_url):
        requests.get(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={img_url}')

    # Второй способ: Отправить файл с компьютера (максимальный размер фотографий - 10 МБ, для остальных файлов - 50 МБ).
    def send_photo_file(chat_id, img):
        files = {'photo': open(img, 'rb')}
        requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files)

    # Третий способ: Отправить, передав в параметрах file_id файла который уже хранится где-то на серверах Telegram (ограничений нет).
    def send_photo_file_id(chat_id, file_id):
        requests.get(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={file_id}')

    # Таким образом вы можете отправить документ, видео, или аудиофайл заменив в URL метод sendPhoto на подходящий.
    # sendVoice Используйте этот метод для отправки аудиофайлов, если вы хотите, чтобы клиент Telegram отображал файл как воспроизводимое голосовое сообщение.
    # sendDocument Используйте этот метод для отправки общих файлов.
    # sendAudio Используйте этот метод для отправки аудиофайлов, если вы хотите, чтобы клиент Telegram отображал их в музыкальном проигрывателе.
    # sendVideo Используйте этот метод для отправки видеофайлов, клиент Telegram поддерживают видео в формате mp4 (другие форматы могут быть отправлены как документ ).
    # sendPhoto Используйте этот метод для отправки фотографий.
    # Полный список методов https://core.telegram.org/bots/api

    # =====================
    # Встроенная клавиатура
    # =====================
    # InlineKeyboardMarkup - Этот объект представляет собой встроенную клавиатуру, которая появляется рядом с отправленным сообщением.
    def inline_keyboard(chat_id, text):
        # массив строк кнопок, каждая из которых представлена массивом объектов InlineKeyboardButton
        reply_markup = {'inline_keyboard': [
            [{'text': 'Сайт____________________1', 'url': 'https://www.lenta.ru'}, {'text': 'Сайт____________________2', 'url': 'https://www.soccer.ru'},
             {'text': 'Сайт____________________3', 'url': 'https://www.mail.ru'}], [{'text': 'Сайт____________________1', 'url': 'https://www.lenta.ru'}, {'text': 'Сайт____________________2', 'url': 'https://www.soccer.ru'},
             {'text': 'Сайт____________________3', 'url': 'https://www.mail.ru'}]]}
        data = {'chat_id': chat_id, 'text': text, 'reply_markup': json.dumps(reply_markup)}
        requests.post(f'{URL}{TOKEN}/sendMessage', data=data)
        time.sleep(1)
        data = {'chat_id': chat_id, 'text': text}
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
                chat_id = message['message']['chat']['id']
                # print(f"Чат ID {chat_id}")
                check_message(chat_id, message['message']['text'])
                # print(f"ID пользователя: {message['message']['chat']['id']}, Сообщение: {message['message']['text']}")