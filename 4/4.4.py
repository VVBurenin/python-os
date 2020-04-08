list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [list1[i] for i in range(0, len(list1)) if list1.count(list1[i]) < 2]
print(new_list)
