"""
Программа принимает действительное положительное число ​x и целое отрицательное число y.
Необходимо выполнить возведение числа ​x в степень​y.
Задание необходимо реализовать в виде функции ​my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


#def my_func(x, y):
#    return x ** y


#print(my_func(5, -3))
#print(5 ** (-3))


def my_func1(x, y):
    z = 1
    while y != 0:
        z = z * x
        y += 1
    return 1 / z

print(my_func1(5,-3))