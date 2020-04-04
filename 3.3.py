def twomax(var1, var2, var3):
    list_twomax = [var1, var2, var3]
    list_twomax.sort()
    list_twomax.reverse()
    print(list_twomax)
    return float(list_twomax[0]) + float(list_twomax[1])


sum_user = twomax(10, 20, 5)
print(sum_user)
