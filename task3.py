# Напишите программу, 
# которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


import math

a = input('enter number:\n')
def my_sum(s):
    return sum(map(lambda x: int(x) if x.isdecimal() else 0, s))

print(my_sum(a))