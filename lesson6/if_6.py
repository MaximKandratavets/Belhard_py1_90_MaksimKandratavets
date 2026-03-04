"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""
a1, a2, a3, a4 = input(), input(), input(), input()

if ('.' in a1 and a1.replace('.', '', 1).isdigit() and
    '.' in a2 and a2.replace('.', '', 1).isdigit() and
    '.' in a3 and a3.replace('.', '', 1).isdigit() and
    '.' in a4 and a4.replace('.', '', 1).isdigit()):
    print(True)

elif (not a1.replace('.', '', 1).isdigit() or
      not a2.replace('.', '', 1).isdigit() or
      not a3.replace('.', '', 1).isdigit() or
      not a4.replace('.', '', 1).isdigit()):
    print(True)

elif ((a1.isdigit() and a3.isdigit()) or  
      (a2.isdigit() and a4.isdigit()) or  
      (a3.isdigit() and a4.isdigit())):   
    print(True)

else:
    print(False)