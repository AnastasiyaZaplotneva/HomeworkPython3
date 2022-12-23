# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
numbers = list()
for i in range(0,7):
    numbers.append(random.randint(1, 20))
print(numbers)
sum = 0
for idx, item in enumerate(numbers):
    if idx % 2:
        sum += item
print(sum)