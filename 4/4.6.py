from itertools import count
from itertools import cycle
from sys import argv

script_name = argv
user_star = int(input('Введите начало цикла: '))
new_list = []
for i in count(user_star):
    if i < 10:
        if i % 2 == 0:
            new_list.append(i)
            print(i)
    else:
        break

c = 0
for i in cycle(new_list):
    if c < len(new_list):
        print(i)
        c += 1
    else:
        print('Конец')
        break