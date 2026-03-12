'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

def count_m(n):
    if n == 0: return '0'
    
    groups = []
    current_group = []
    
    while n > 0:
        last_num = n % 10
        current_group.append(str(last_num))
        n = n // 10
        
        if len(current_group) == 3:
            groups.append(''.join(current_group[::-1]))
            current_group = []
    
    if current_group:
        groups.append(''.join(current_group[::-1]))
        groups = ' '.join(reversed(groups))
    return f'{groups}.00 руб'
n = int(input())
print(count_m(n))