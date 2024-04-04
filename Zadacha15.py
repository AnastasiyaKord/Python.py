"""
Задача №15. Общее обсуждение
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

n = int(input())
max = -1 # переменная, где хранится мах вес арбуза.Берем число(вес арбуза) мин-но возможное, поэтому -1.
min = 30001 # переменная, где хранится минимальный вес арбуза. Берем максимальное число, которое возможно 30001.
for i in range(n): # цикл, где при каждой итерации мы будем вводить вес арбуза
    x = int(input())
    if x > max: # если наше число х больше, чем наше максимально число, то наша переменная мах = переменной х
        max = x
    if x < min: # если наша переменная меньше, чем наше мин число, то мы делаем переприсваивание
        min = x # переприсваивание
print(max, min)
