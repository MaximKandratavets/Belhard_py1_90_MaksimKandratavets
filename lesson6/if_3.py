'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''
num1, num2, num3 = (
    int(input('Введите 1-е число: ')),
    int(input('Введите 2-е число: ')),
    int(input('Введите 3-е число: '))
)                   
res = (
    num1 if num1 >= num2 and num1 >= num3 else
    num2 if num2 >= num1 and num2 >= num3 else
    num3 if num3 >= num1 and num3 >= num2 else
    'Не верно введены данные'
)
print(res)