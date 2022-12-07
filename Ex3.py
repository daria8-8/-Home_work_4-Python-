# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


import random
lst =[]
for i in range(20):
    lst.append(random.randint(0,15))
print(f'Исходная последовательность чисел:\n{lst}')
new_list =[]
for i in lst: 
    if lst.count(i)==1:
        unique=i
        new_list.append(unique)
print(f'Список уникальных элементов исходной последовательности:\n{new_list}')
new_list_1 =[]
for i in lst: 
    if i not in new_list_1:
        new_list_1.append(i)
print(f'Список неповторяющихся элементов исходной последовательности:\n{new_list_1}')

