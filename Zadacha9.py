"""
Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120 
"""
n = int(input())
i = 1 # счетчик цикла (переменная), она будет определять, когда нам нужно выйти из цикла while
result = 1 # переменная, где мы будем хранить наш результат
while i <= n: # цикл
    result *= i # умножаем на единицу, потому что если умножить на ноль, то получим ноль
    i += 1 # переменную i увеличиваем на единицу
print(result)