#! /usr/bin/env python3
# dictionary.py

# Dictionary
grades = {"chemistry" : 10 , "history" : 8 , "math" : 9}
print(len(grades))

# Procurar algo
print("Nota de matematica: {}".format(grades["math"]))

# Adicionando elementos
grades["English"] = 8
print(len(grades))
print(grades)

# Deletando o elemento
del grades["math"]
print(grades)