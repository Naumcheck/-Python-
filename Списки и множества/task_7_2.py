'''

В переменной numbers_list сохранен список с целыми числами. В списке минимум два разных целых числа.

В переменную numbers_list_ordered сохраните все числа из списка numbers_list, отсортированные по убыванию. При этом сам список numbers_list не должен изменяться.

В переменную numbers_set сохраните множество из уникальных чисел из списка numbers_list. Дополните это множество следующим целым числом после максимального числа из numbers_list.

В переменную numbers_frozenset сохраните неизменяемое множество из всех уникальных чисел из списка numbers_list, кроме минимального числа.

'''
numbers_list_ordered = sorted(numbers_list, reverse = True)
numbers_set = set(numbers_list)
numbers_set.add(max(numbers_list) + 1)
numbers_frozenset = set(numbers_list)
numbers_frozenset.discard(min(numbers_list))
numbers_frozenset = frozenset(numbers_frozenset)