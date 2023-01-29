#
import json
import requests
from random import randint
import time


def get_vacancy(vacancy_id):
    base_url = 'https://api.hh.ru/'
    extra_url = f'vacancies/{vacancy_id}'
    response = requests.get(base_url + extra_url)
    # print(response.status_code)
    if (response.ok):
        return response.json()

# парсер vacancy.json. на выходе список всех значений по ключу f_key
def parse(s_dict: dict, f_key, list_keys, list_dict: list):
    if len(list_dict) > 0:
        for list_instance in list_dict:
            parse(list_instance, f_key, list_keys, [])
    for key in s_dict.keys():
        # print(key)
        if key == f_key:
            list_keys.append(s_dict.get(key))
        if (isinstance(s_dict.get(key), dict)):
            parse(s_dict.get(key), f_key, list_keys, [])
        elif (isinstance(s_dict.get(key), list)):
            parse({}, f_key, list_keys, s_dict.get(key))
    return list_keys



# нужно остановить выполнение рекурсии при нахождении нужного по счёту ключа
# парсер vacancy.json. на выходе значение по ключу f_key и его порядковому номеру в json
def parse_number(s_dict: dict, f_key, serial_number, list_keys, list_dict: list):
    if len(list_dict) > 0:
        for list_instance in list_dict:
            parse_number(list_instance, f_key, serial_number, list_keys, [])
    for key in s_dict.keys():
        print(key)
        if key == f_key:
            list_keys.append(s_dict.get(key))
            print(len(list_keys))
            if len(list_keys) == serial_number:
                print(list_keys[-1])
        if (isinstance(s_dict.get(key), dict)):
            parse_number(s_dict.get(key), f_key, serial_number, list_keys, [])
        elif (isinstance(s_dict.get(key), list)):
            parse_number({}, f_key, serial_number, list_keys, s_dict.get(key))
    return list_keys


# dump() для записи данных в файлы
# dumps() для записей в строку Python

# data = {'1':
#     {
#         '11': 'Одиннадцать',
#         '12': 'Двенадцать'
#     },
#     '2': 'Два'}

# json_file = 'json_files/data.json'
# with open(json_file, 'w') as write_file:
#     json.dump(data, write_file)
#
# json_string = json.dumps(data, indent=4)
# # print(json_string)
#

# json_file = 'json_files/vacancy.json'
# with open(json_file, 'r', encoding='utf-8') as read_file:
#     data = json.load(read_file)
# print(data)
#
# # ключ
# f_key = 'salary'
# parse_result = parse(data, f_key, [], [])
# print(f'Парсинг - {parse_result}')
# key_1 = 'from'
# key_2 = 'to'
# print(f'Зарплата от {parse_result[0].get(key_1)} до {parse_result[0].get(key_2)}')

# f_key = 'id'
# serial_number = 2
# parse_result = parse_number(data, f_key, serial_number, [], [])
# print(f'Парсинг - {parse_result}')

# # print(get_vacancy('72226080'))
# json_file = 'json_files/vacancy_3.json'
# with open(json_file, 'r', encoding='utf-8') as read_file:
#     data = json.load(read_file)
# f_key = 'salary'
# parse_result = parse(data, f_key, [], [])
# print(f'Парсинг - {parse_result}')
# f_key = 'name'
# parse_result = parse(data, f_key, [], [])
# print(f'Парсинг - {parse_result[1]}')
# key_1 = 'from'
# key_2 = 'to'
# print(f'Зарплата от {parse_result[0].get(key_1)} до {parse_result[0].get(key_2)}')

for i in range(1):
# ============================================
    id_vacancy = str(randint(10000000, 70000000))
    # print(id_vacancy)
    # data = get_vacancy('72226080')
    data = get_vacancy(id_vacancy)
    if data!=None:
        print(data)
        print()
        f_key = 'employer'
        parse_result = parse(data, f_key, [], [])
        print(f'Зарплата - {parse_result}')
        f_key = 'name'
        parse_result = parse(data, f_key, [], [])
        print(f'Должность - {parse_result[1]}')
    # при задержке менее 0.6 секунд HH.ru иногда присылает что попало
    time.sleep(0.6)


# key_1 = 'from'
# key_2 = 'to'
# print(f'Зарплата от {parse_result[0].get(key_1)} до {parse_result[0].get(key_2)}')

