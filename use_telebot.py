# PythonBot_First_ToDo
# Используем фреймворк pyTelegramBotAPI
# вся документация на английском языке https://pypi.org/project/pyTelegramBotAPI/
import telebot
import re
import wikipedia
from dotenv import load_dotenv
import os
from pathlib import Path
import bot_1
import bot_2
import bot_3
import bot_4
import bot_5

def get_TOKEN():
    # Хранение TOKEN в отдельном файле .env. Он добавляется в исключения .gitignore и не выгружается на GitHub
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    TOKEN = os.getenv("TOKEN")
    return TOKEN

def toDoFamily(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    # Обработчик сообщений
    @bot.message_handler(content_types=["text"])
    def echo(message):
        human_message = message.text.lower()
        names_parents = ['никита', 'папа', 'анна', 'аня', 'мама']
        names_children = ['анастасия', 'настя', 'екатерина', 'катя', 'александр', 'саша']
        find_name = False
        for name in names_parents:
            if name in human_message:
                bot.send_message(message.chat.id, f'Давно не виделись, {name.capitalize()}! Пора бахнуть!!!')
                find_name = True
        for name in names_children:
            if name in human_message:
                bot.send_message(message.chat.id, f'Привет, {name.capitalize()}!!! Время позднее, пора баиньки.')
                find_name = True
        if not find_name:
            bot.send_message(message.chat.id, f'Ты мне пишешь "{message.text}", а я тебя не знаю...')

            # bot.send_message(message.chat.id, f'Ты мне пишешь {message.text}, а я тебя не знаю')

            # bot.send_message(message.chat.id, message.text)

    # Постоянно обращается к серверам Telegram
    bot.polling(non_stop=True)


def echo_bot(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    # Функция, обрабатывающая команду /start
    @bot.message_handler(commands=["start"])
    def start(message, res=False):
        bot.send_message(message.chat.id, 'Я на связи. Напиши мне что-нибудь )')

    # Получение сообщений от юзера
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

    # Запускаем бота
    bot.polling(none_stop=True, interval=0)


def wikipedia_bot(TOKEN):
    # Создаем экземпляр бота
    bot = telebot.TeleBot(TOKEN)
    # Устанавливаем русский язык в Wikipedia
    wikipedia.set_lang("ru")

    # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
    def getwiki(word):
        try:
            ny = wikipedia.page(word)
            # print(ny)
            # Получаем первую тысячу символов
            wikitext = ny.content[:1000]
            # Разделяем по точкам
            wikimas = wikitext.split('.')
            # Отбрасываем всЕ после последней точки
            wikimas = wikimas[:-1]
            # Создаем пустую переменную для текста
            # print(*wikimas)
            wikitext2 = ''
            # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
            for x in wikimas:
                if not ('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                    if (len((x.strip())) > 3):
                        wikitext2 = wikitext2 + x + '.'
                else:
                    break
            # Теперь при помощи регулярных выражений убираем разметку
            # wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
            # wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
            # wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
            # Возвращаем текстовую строку
            return wikitext2
        # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
        except Exception as e:
            return 'В энциклопедии нет информации об этом'

    # Функция, обрабатывающая команду /start
    @bot.message_handler(commands=["start"])
    def start(message, res=False):
        bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')

    # Получение сообщений от юзера
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        # Запись логов
        # print(f'{str(message.chat.id)}_log.txt')
        with open(f'{str(message.chat.id)}_log.txt', 'a', encoding='UTF-8') as f:
            f.write(f'u: {message.text}\n')

        bot.send_message(message.chat.id, getwiki(message.text))

    # Запускаем бота
    bot.polling(none_stop=True, interval=0)


def two_virtual_buttons(TOKEN):
    pass


def joke_bot(TOKEN):
    pass




if __name__ == '__main__':
    TOKEN = get_TOKEN()
    # toDoFamily(TOKEN)
    # echo_bot(TOKEN)
    # wikipedia_bot(TOKEN)
    # bot_1.bot_start(TOKEN)
    # bot_3.bot_start(TOKEN)
    # bot_3.bot_start(TOKEN)
    # bot_4.bot_start(TOKEN)
    bot_5.bot_start(TOKEN)