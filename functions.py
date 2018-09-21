#! /usr/bin/env python3
# functions.py

#  ----------------- Definição de uma funçao que retona o quadrado de uma valor -----------------
def function (x):
    return x**2

def function2(x,y):
    return ((x**2 + y**2))

# ----------------- Realizando a chamada das funções -----------------
print("2 ao quadrado é: {}".format(function(2)))
print("Soma do quadrado de 2 e 3: {}".format(function2(2,3)))

# ----------------- Funçao com argumentos pre definidos (deafult) -----------------
def add_user(name, gender="u"):
    if (gender == "u"):
        string = "User " + name + " not added"
    else:
        string = "User " + name + " not successfully"
    return string

print("Log: {}".format(add_user("Valmir", "m")))

# ------------- Funçoes recebendo outras funções -------------------
def f(x):
    return x/2 # x²

def high_g(x, func):
    return func(x)

def h(string):
    return "'" + string + "'" + " Was your message"

print(high_g(2,f)) # Result will be 4

# ----------------- Listas de funções. Cada elemento é uma -----------------
Functions = [f, high_g, h]

print("Função f: {}".format(Functions[0](3))) # Result will be 9
print("Função high_g: {}".format(Functions[1](4, Functions[0]))) # Result will be 16
print("Função h: {}".format(Functions[2]("Hi"))) # Result will be: 'Hi' Was your message

# ------------- USO DE LAMBDA (função rapida de criar) -------------------
a = lambda x: x+10
print(a(10)) # Will be 20
print((lambda x: x+10)(10)) # Will be 20

# ----------------- Loop gerando lista --------------------------
print([x**2 for x in range(10) if x % 1 == 0]) # Se x for par, faça x², com loop x = 0 até x < 10
print([f(x) for x in range(10) if x % 2 == 0])