def custom_write(file_name, string):
    with open(file_name, 'w', encoding='utf-8') as file:
        string_positions = {}
        for i, string in enumerate(string, 1):
            file.write(string + '\n')
            string_positions[(i, file.tell() - len(string) - 1)] = string
        file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)