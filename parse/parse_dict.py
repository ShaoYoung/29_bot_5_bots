def __get_value_by_key(data: dict, lst: list) -> str | int | bool:
    '''
    Функция, которая из словаря вытаскивает объекты по списку ключей. На вход передавать словарь и список ключей
    :param data: словарь
    :param lst: список ключей
    :return: значение, которое лежит внутри словаря по ключам из списка
    '''
    if not lst or not isinstance(data, dict):
        return data
    return __get_value_by_key(data.get(lst[0]), lst[1:])

data = {'1':
    {
        '11': 'Одиннадцать',
        '12': 'Двенадцать'
    },
    '2': 'Два',
    '3':
        {
            '31':'Тридцать один',
            '32':'Тридцать два'
        }
}

# key_list = ['1', '11']
key_list = ['3', '32']

print(__get_value_by_key(data, key_list))


