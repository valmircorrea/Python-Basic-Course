#! /usr/bin/env python3
# loops.py

# Retorna de 0 até 5
print(range(5))

# For
for ii in range(5):
    print(ii)

# somatorio de 0 até 5, somando 2 a cada interação
sum = 0
for ii in range(0, 5, 2):
    print("Valor de ii: {}".format(ii))
    print("Valor de sum: {}".format(sum))
    sum = sum + ii
    print("Valor de sum + ii: {}".format(sum))
    
print("Soma: {}".format(sum))

# While
pp = 0
while pp < 5:
    print(pp)
    pp = pp + 1
    
ll = 8
while (True):
    if ((ll % 51) == (ll % 7)):
        print(ll)
        break
    else:
        ll = ll + 1
        continue            # nesse caso é opcional

# Imprimindo cada elemento de uma lista
numbers = [2, 3, 4, 7, 8]
for x in numbers:
    print(x);

# Imprimindo cada elemento de um dicionario kk = nome e vv = nota
grades = {"chemistry" : 10 , "history" : 8 , "math" : 9}
for kk, vv in grades.items():
    if vv >= 9:
        print("You have an A in: " + kk)
    else:
        print("Study more in: " + kk)
        
