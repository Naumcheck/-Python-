'''

Дан словарь dict_input. Поменяйте ключи и значения местами. Результат сохраните в result. 


'''
key = dict_input.keys()
val = dict_input.values()
result = dict(zip(val, key))