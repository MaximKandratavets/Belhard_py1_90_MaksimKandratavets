"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""
d = {'one':11, 'two':22, 'hello':'python', True:False}
el_dict = input(
    f'Напишите номер элемента из перечисленных которые хотите удалить {list(d.keys())}: '
)
del d[el_dict]
print(*d)