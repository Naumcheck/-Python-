'''

В переменной a хранится список целых неотрицательных чисел. Количество чисел четное.
Напишите программу, которая будет делить этот список пополам, определять суммы чисел в половинах списка (sum_left и sum_right). 
Если sum_left равно sum_right, то сохраните в переменную result значение True,  в противном случае — False. 


'''
n = len(a) // 2
result = False
sum_left = sum(a[:n])
sum_right = sum(a[n:])
if sum_right == sum_left :
    result = True