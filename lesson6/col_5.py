"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""
s = input('Введите фразу: ').split()
symb = ' '.join(s).lower()
symb = list(symb.replace(' ', ''))
set_symb = set(symb)
count_symb = list(map(symb.count, set_symb)) 
zip_symb = dict(zip(set_symb, count_symb))
print(count_symb)
print(set_symb)
print(
    f'Уникальных символов: {len(set_symb)}',
    f'Уникальных слов: {len(set(s))}',
    f'Символ который встречался чаще всего: {max(zip_symb.items(), key=lambda x: x[1])}', sep='\n'
)