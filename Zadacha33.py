"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

n = int(input()) # вводим кол-во элементов массива
list1 = list() # создаем список
for i in range(n): # далее заполняем цикл с помощью цикла
    x = int(input()) # при каждой итерации цикла будем вводить число х и добавлять его в список
    list1.append(x)
max_n = max(list1) # встроенные функции в Python, чтобы найти мах элеемент, мы применяем функцию max
min_n = min(list1) # функция min
for i in range(len(list1)): # len - размер списка. Создаем цикл, в котором будем проходиться по каждому элементу и будем проверять, если элемент равен мах, то мы заменим его на min
    if list[i] == max_n: # при каждой итерации цикла делаем проверку, если текущий элемент списка равен мах, то делаем замену и теперь текущий элемент списка равен min числу
        list[i] = min_n
print(list1) # выводим список