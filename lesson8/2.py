'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

def accept_rectangle(a, b, find):
    if find == 'площадь':
        return a * b
    elif find == 'периметр':
        return 2 * (a + b)


try:
    a, b = map(int, input('Введите через пробел две стороны прямоугольника: ').split())
    assert a > 0 and b > 0, 'Ошибка: Стороны должны быть больше нуля!'
except ValueError:
    print("Ошибка: Данные введены не корректно")
    exit()
except AssertionError as e:
    print(e)
    exit()

try:
    find = input('Введите что хотите найти периметр или площадь треугольника: ').lower()
    assert find in ('площадь', 'периметр'), 'Ошибка: Некорректно введены данные'
except AssertionError as r:
    print(e)
    exit()

print(f'Результат: {accept_rectangle(a, b, find)}')
