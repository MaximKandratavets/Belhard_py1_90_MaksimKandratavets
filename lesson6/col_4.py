'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''
letter = {'a': 10, 'b': 20, 'c': 30, 'd': 40 }
count_letter= [input(f'Введите 1-ю из 5-и букв: {list(letter.keys())} - ').lower(),
                     input(f'Введите 2-ю из 5-и букв: {list(letter.keys())} - ').lower(),
                     input(f'Введите 3-ю из 5-и букв: {list(letter.keys())} - ').lower(),
                     input(f'Введите 4-ю из 5-и букв: {list(letter.keys())} - ').lower(),
                     input(f'Введите 5-ю из 5-и букв: {list(letter.keys())} - ').lower()
]
result = list(map(lambda x: letter.get(x), count_letter))
print(f'Сумма очков введенной фразы: {sum(result)}')