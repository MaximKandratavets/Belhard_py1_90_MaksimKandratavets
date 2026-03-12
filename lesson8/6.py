"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

def yes_or_no(s):

    list_n = []
    list_clone = []

    for i in s:
        try:
            if int(i):
                if i not in list_clone:
                    list_n.append('no')
                    list_clone.append(i)
                    continue

                list_n.append('yes')
        except  ValueError:
            list_n.append(False)
    return list_n

s = input()

print(yes_or_no(s))
        

