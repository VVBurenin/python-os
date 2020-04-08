from sys import argv

script_name, first_param, second_param, third_param = argv
wages = int(first_param) * int(second_param) + int(third_param)
print('Выроботка в часа:', first_param)
print('Ставка в час: ', second_param)
print('Премия: ', third_param)
print('Итого заработная плата рабочие часы: ', wages)
