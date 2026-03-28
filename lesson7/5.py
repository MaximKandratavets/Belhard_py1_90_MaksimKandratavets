'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''
list_task = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
for i in range(len(list_task)):
    print(f'{i + 1} - {list_task[i]} - {list_task[i][i]}')