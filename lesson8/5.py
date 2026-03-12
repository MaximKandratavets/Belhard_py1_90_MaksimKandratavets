'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

def count_char(s):
    dict_w = {}
    for i in s:
        count = 0
        if i == ' ':
            continue

        for j in range(len(s)):
            if s[j] == i:
                count += 1

        dict_w[i] = count

    return dict_w

try:
    s = input('Напишите строку: ').strip()
    assert s != '', 'Ошибка: введите непустую строку!'
except AssertionError as e:
    print(e)
print(count_char(s))

