"""
Сортировка слиянием
"""
def merge_sort(nums): # создаем функцию - сортировка слиянем и будем туда передавать значения nums - наш список
    if len(nums) > 1: # здесь будем проверять, если длина nums больше 1, то мы что-то делаем
        mid = len(nums) // 2 # создаем переменную mid? в кт. будет храниться значение(будем брать отттуда только целую часть, это будет наша середина)
        left = nums[:mid] # создаем первый список left - он получается путем обращения к nums и мы будем ьрать только начало - левую часть [ :mid]
        right = nums[mid:] # создаем список где будет храниться правая часть. Обращаемся к списку nums и идем от середины и до конца [mid: ]
        # Теперь нам нужно делить наши списки до конца, пока не останется по одному значению. Мы это будем делать с помощью рекурсии.
        merge_sort(left) # создаем merge_sort, в кт будем вызывать для левой части
        merge_sort(right) # и для правой части
        # Теперь нам нужно все элементы соединить воедино
        i = j = k = 0 # создаем 3 переменные, кт. равны нулю. 
        while i < len(left) and j < len(right): # создаем цикл while в кт. будем класть элементы, но уже последовательно. Цикл будет выполняться до тех пор, пока переменная i будет меньше, чем len(left) и одновременно с этим пока переменная j меньше len(right)
            if left[i] < right[j]: # если элемент из списка left[i] меньше чем right[j]
                nums[k] = left[i] # мы проверили значение left[i]
                i += 1 # к переменной i добавляем единицу
            else: # а иначе мы понимаем, что правый элемент больше
                nums[k] = right[j]
                j += 1
            k += 1 # при каждой итерации нашего цикла мы должны увеличивать нашу переменную k на единицу, чтобы при каждой итерации добавлялось новое значение
        # Мы должны написать условие, что пока у нас есть элементы в левом списке, мы добавляем их в конец. В любом случае у нас будет только одно из двух - либо в левом списке остались элементы либо в парвом. 
        # Потому что мы написали условие, что мы идем в цикле while до тех пор пока в обоих списках есть какое-то значение, если хоть в одном списке значения закончились, то мы выходим из нашего цикла
        while i < len(left): # пока перменная i меньше len(left)
            nums[k] = left[i]
            i += 1
            k += 1
        # и тоже самое делаем для нашего правого списка
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [38, 27, 43, 3, 9, 82, 10] # создаем список list1 и зададим значения
merge_sort(list1) # dspjdtv нашу функцию и передадим значение в наш список list1
print(list1) # выводим список list1