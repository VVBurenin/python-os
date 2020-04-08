def func(int_f):
    for elem in range(1, (int_f + 1)):
        yield elem


n = int(input('Введите число искомого факториала: '))
fact = func(n)
print(fact)
z = 1
for i in fact:
    print('Числа факториала:', i)
    z = z * i
print(f'Факторила чила {n} равен: {z}')
