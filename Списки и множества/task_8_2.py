'''

Даны два списка list_1 и list_2. Отсортируйте list_1 по возрастанию, а list_2 по убыванию. 
Объедините list_1 и list_2 в один отсортированный по возрастанию список list_3.  
В переменную list_3_len сохраните длину  list_3. 

'''
list_1.sort()
list_2.sort(reverse = True)
list_3 = sorted(list_1 + list_2)
list_3_len = len(list_3)