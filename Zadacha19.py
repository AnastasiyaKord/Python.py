"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
"""
list1 = [5, 4, 6, 7, -10] # дана последовательность из N целых чисел
k = int(input()) # вводим число к ( мы знаем, что наше число к может быть больше размера списка).В том случае, если размер списка 5, а число к - у нас будет 6, то мы должны будем сдвинуться только на один элемент, т.к. первые пять у нас будет просто циклический сдвиг, и чтобы лишний раз не сдвигать преобразуем к.
k = k % len(list1) # мы берем остаток от деления на размер нашего списка, т.е., если к будет равна 6, то после нашего преобразования у нас будет к = 1, мы должны будем сдвинуть только один элемент вправо
list_res = [] # создаем результирующий список

for i in range(k): # цикл, в котором мы будем записывать наши первые к-элементов, т.е. те элементы, которые у нас сдвинулись в начало списка. Цикл по к-элементам повторяется к-раз.
    list_res.append(list1[len(list1) - 1 - i]) # при каждой итерации цикла мы в наш результирующий список будем добавлять новые значения, которые сдвинулись влево. Делаем это с помощью функции append и добавляем элемент из списка 1 (будем считать размер нашего списка и вычтем оттуда единицу, т.к. индексация начинается с нуля и вычтем i, т.е. нашу переменную цикла - это нам нужно для того, чтобы мы могли поочередно записывать каждый элемент.)
print(list_res) # вывод результирующего списка

# далее записываем все оставшиеся элементы
for i in range(len(list1) - k): # создаем цмкл и здесь будем записывать те элементы, которые у нас остались. Какое их колличество? Это размер нашего списка миус к, т.к. первый к-элемент мы записали уже в первом цикле.
    list_res.append(list1[i]) # при каждой итерации цикла, мы должны в наш результирующий список добавить значения - list1[i].
print(list_res) # вывод результата

