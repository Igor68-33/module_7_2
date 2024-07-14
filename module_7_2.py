# "Позиционирование в файле"

def custom_write(file_name, strings):
    """
    Записывает в файл file_name все строки из списка strings
    :param file_name:
    :param strings: [str]
    :return strings_positions: {(<номер строки>, <байт начала строки>): записываемая строка}
    """
    rez = dict()
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(0, len(strings)):
        rez.update({(i + 1, file.tell()): strings[i]})
        file.write(strings[i] + '\n')
    file.close()
    return rez


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
