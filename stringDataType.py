#! /usr/bin/env python3
# stringDataType.

#  -------- Verificando o tipo da variavel
name = "Valmir"
print("\t Tipo da variavel: {}".format(type(name)))

quote = "\" How do you do\" "
print(quote)
quote = '"How do you do?"'
print(quote)

# -------- Quebra de linha
newLine = "Line\n New line"
print(newLine)

# -------- Tab
newTab = "column1\t column2"
print(newTab)

# -------- Concaternação de strings
add = "hello" + " " + "there!"
print(add)

# ----------------- Metodos -----------------

# Acessando letra "h" da string (index)
print(add[0])  

# Retornando a string a partir de 2 até 6
print(add[2:6])

# Tamanho da string
print(len(add))

# Transformando strings em minusculas
print(add.lower())

# Transformando strings em maisculas
print(add.upper())

# Verificando string ou char dentro de uma string
print("l" in add)

# Verificando string ou char não esta dentro de uma string
print("a" not in add)

