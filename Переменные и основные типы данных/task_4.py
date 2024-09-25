"""
Заданы вещественные числа a, b и с – стороны треугольника. 
Вычислите периметр и площадь треугольника. Результат сохраните в переменные perimeter и area соответственно.
"""

perimeter = (a + b + c) / 2
area = pow((perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c)), 0.5)
perimeter = a + b + c