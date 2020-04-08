from functools import reduce

new_list = [i for i in range(100, 1001) if i % 2 == 0]


def my_func(el1, el2):
    return el1 * el2


print(reduce(my_func, new_list))
