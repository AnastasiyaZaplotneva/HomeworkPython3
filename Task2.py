# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import math
numbers = list()
for i in range(0,7):
    numbers.append(random.randint(1, 10))
print(numbers)
product_of_numbers = list()
j = -1
for i in range(math.ceil(len(numbers)/2)):
    product_of_numbers.append(numbers[i]*numbers[j])
    j += -1
print(product_of_numbers)
