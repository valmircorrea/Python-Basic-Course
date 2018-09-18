#! /usr/bin/env python3
# list.py

# lista
my_list = [2, 4, 6]
print(my_list)

# tamanho
print(len(my_list))

# Add elemnt no final
my_list.append(8)
print(my_list)

# Acessando primeiro elemento
print(my_list[0])

# Imprimindo duas listas uma apos a outra
other_list = [10, 12, 14, 16]
print(my_list + other_list)

# Imprime o vetor N vezes
a = [1, 2, 3]
b = a * 3
print(b)

# Verificando elemento na lista
print(4 in a)
