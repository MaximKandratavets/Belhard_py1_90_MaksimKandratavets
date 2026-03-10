'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''

login_uss  = input('Введите ваш логин: ')
pass_uss = input('Введите ваш пароль: ')
age_uss = int(input('Введите ваш возраст: '))
res = (
       'Доступ разрешен' if login_uss == 'admin' 
       and pass_uss == '123456' else
       'Доступ разрешен' if login_uss == 'vasya' 
       and pass_uss == 'vas123' 
       and age_uss < 60 else
       'Доступ разрешен' if login_uss == 'guest' and 18 < age_uss else
       'Доступ запрещен'
)
print(res)
# elif  login_uss == 'vasya' and pass_uss == 'vas123' and age_uss < 60:
#     print('Доступ разрешен')
# elif login_uss == 'guest' and 18 < age_uss:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')