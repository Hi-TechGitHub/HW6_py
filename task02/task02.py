#Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint as RI
list1 = []
list2 = []
size = int(input('Enter size: '))
first = int(input('Enter num: '))
last = int(input('Enter num: '))
for _ in range(size):
    list1.append(RI(-10, 20))

for i in range(size):
    if list1[i] < last and list1[i] > first:
        tag = list1[i]
        list2.append(list1.index(tag))
print(list1)
print(list2)