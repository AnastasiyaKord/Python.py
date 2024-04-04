#мы обращаемся к модулю
import modul1Lekciya3
print(modul1Lekciya3.max1(10, 9))

#если мы хотим напрямую обратиться к функции:
from modul1Lekciya3 import max1
print(max1(10, 9))

# если мы хотим импортировать все функции сразу, то ставим *
from modul1Lekciya3 import *
print(max1(10, 9))

#можно переименовать модуль, чтобы легче и коротко было писать
import modul1Lekciya3 as m1
print(m1.max1(10, 9))