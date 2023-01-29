# бот_1
import telebot


def bot_start(TOKEN):
    bot = telebot.TeleBot(TOKEN)
    # Декоратор, обрабатывающий команду /start и др. (список строк). команды в боте пишутся через /
    @bot.message_handler(commands=['start', 'старт'])
    #     функцию лучше называть также, как и обрабатываемую команду от бота. message - сообщение от пользователя
    def start(message):
        # можно отправить не только сообщение, а также стикер, аудио, документ и т.д.
        # 2 обязательных параметра: чат и сообщение. parse_mode - режим парсинга сообщения
        # если parse_mode не указан, то по умолчанию он = 'text'
        mess = f'<b>Привет, {message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        # открываем файл в photo

    # если декоратор без параметров, то он обрабатывает все сообщения от пользователя.
    # лучше указывать параметр content_types @bot.message_handler(content_types=['text'])
    # @bot.message_handler(content_types=['text'])
    def get_user_text(message):
        # можно посмотреть сообщение целиком. все поля там.
        # bot.send_message(message.chat.id, message, parse_mode='html')
        if message.text == 'Привет':
            mess = 'Привет'
        elif message.text == 'id':
            mess = f'Твой id {message.from_user.id}'
        elif message.text == 'username':
            mess = f'Твой username {message.from_user.username}'
        elif message.text == 'photo':
            photo = open('photo/Good_Job.png', 'rb')
            bot.send_photo(message.chat.id, photo)
            mess = 'Cool photo!'
        else:
            mess = message
        # bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.send_message(message.chat.id, mess)

    # декоратор, отслеживающий контент определённого типа. список. можно задавать несколько типов
    # The Message object also has a content_typeattribute, which defines the type of the Message. content_type can be one of the following strings: text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message, web_app_data.
    @bot.message_handler(content_types=['photo'])
    def get_user_photo(message):
        bot.send_message(message.chat.id, 'Крутое фото!')

    @bot.message_handler(commands=['website'])
    def website(message):
        # разметка. тип - Inline-клавиатура, встроенная в сообщение
        markup = telebot.types.InlineKeyboardMarkup()
        # добавить кнопку
        markup.add(telebot.types.InlineKeyboardButton('Посетить веб сайт', url='https://gb.ru/lessons/286606/homework'))
        # аргумент reply_markup - разместить разметку. текстовое сообщение обязательно
        bot.send_message(message.chat.id, 'Нажми', reply_markup=markup)

    @bot.message_handler(commands=['help'])
    def website(message):
        # разметка. тип - Reply-встроенные в поле ввода ответа вещи (кнопки, изображения и т.д.)
        # resize_keyboard - автоопределение нужного размера кнопок
        # row_width - сколько кнопок в одном ряду (max)
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        # создаём кнопки
        site = telebot.types.KeyboardButton('Веб сайт')
        start = telebot.types.KeyboardButton('Старт')
        go = telebot.types.KeyboardButton('Пошли')
        markup.add(site, start, go)
        # аргумент reply_markup - разместить разметку. текстовое сообщение обязательно
        bot.send_message(message.chat.id, 'Query', reply_markup=markup)


    # запуск бота (без остановки при возникновении ApiException)
    bot.polling(none_stop=True)

# список команд бота можно настроить с @BotFather/Edit Bot/Edit Commands