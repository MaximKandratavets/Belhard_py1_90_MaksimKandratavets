'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''
def factorial_num(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


try:
    num = input('Введите число: ')
    num = int(num)
except ValueError:
    print('Ошибка: Введите число !')
    exit()

print(factorial_num(num))