"""
Задача №37. Решение в группах
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""
def f(n): # создаем функцию
    if n == 0: # делаем проверку
        return '' # возвращаем пустую строку(место где выход рекурсии)
    k = int(input()) # вводим число, где -к наша последовательность
    return f(n-1) + f'{k}' # dspsdftv рекурсию, f(n-1) - мы будем уходить дальше и записывать новые результаты и добавляем число -к
#           +''     + '4'     + '3'
n = int(input()) 
print(f(n))