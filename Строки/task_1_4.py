'''

В переменных str_1 и str_2 сохранены две строки. Если все буквы в строках одинаковые, вам нужно сохранить в переменную is_the_same_letters значение True, если буквы в строках отличаются —сохраните в переменную значение False.

Мы не учитываем порядок букв, их количество и регистр. Сами переменные уже созданы, начинайте сразу готовить код для работы с ними.

Примеры:

str_1 = 'AaB'
str_2 = 'Ab'
is_the_same_letters = True 

str_1 = 'Aa'
str_2 = 'AaB'
is_the_same_letters = False

'''
if set(str_1.lower()) != set(str_2.lower()):
    is_the_same_letters = False
else:
    is_the_same_letters = True