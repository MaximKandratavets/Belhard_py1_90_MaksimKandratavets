"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""
estimation = None
list_est = []
while estimation != 0:
    estimation = int(input('Введите оценку ученику: '))
    list_est.append(estimation)
print(sum(list_est) // len(list_est))
