# Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 8
m = 1
n = 8

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))


list=[1, 3, 6, 9, 9, 6]
size

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,2
import math

a = list(map(int,input('Введите координаты точки А= ').split()))
b =list(map(int,input ('Введите координаты точки В= ').split()))
len_line=round(math.sqrt((a[1]-a[0])**2+(b[1]-b[0])**2),2)
print(a)
print(b)

print(len_line)