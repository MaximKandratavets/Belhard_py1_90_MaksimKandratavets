"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""
def format_fio(fio, short_first=False):
    parts = fio.strip().split()
    if len(parts) != 3:
        return 'Ошибка: Введите Фамилию имя Отчество'
    surname, first, patronymic = parts
    first_initial = first[0].upper() + '.'
    part_initial = patronymic[0].upper() + '.'
    if short_first:
        return f'{first_initial}{part_initial} {surname}'
    else:
        return f'{surname} {first_initial}{part_initial}'
fio = input('Введите Фамилию имя и Отчество: ')
short_first = input('Введите 1 если хотите вывести формат ФИО ' \
'или введите 2 для формата ИОФ: ')
if short_first == '1':
    short_first = False
if short_first == '2':
    short_first = True
print(format_fio(fio, short_first))