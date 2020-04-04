def twoargs_del():
    try:
        var1 = float(input('Введите делимое: '))
        var2 = float(input('Введите делитель: '))
    except ValueError:
        print('Вы ввели не число')
        ''' При заполнении типа str вылетает ошибка "UnboundLocalError"'''
    try:
        return (var1 / var2)
    except ZeroDivisionError:
        print('деление на "0" запрещено')


user_del = twoargs_del()

print(user_del)
