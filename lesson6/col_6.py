'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''

num1 = list(map(int, input('Введите несколько чисел через пробел: ').split()))
num2 = list(map(int, input('Введите несколько чисел через пробел: ').split()))
num3 = list(map(int, input('Введите несколько чисел через пробел: ').split()))
uniq_num = set(num1) & set(num2) & set(num3)
only_1 = set(num1) - (set(num2) | set(num3))
only_2 = set(num2) - (set(num1) | set(num3))
only_3 = set(num3) - (set(num1) | set(num2))
res = only_1 | only_2 | only_3
print(*sorted(set(num1) | set(num2) | set(num3)), sep=' ')
print(*uniq_num, sep=' ')
print(*res)
