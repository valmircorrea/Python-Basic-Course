#! /usr/bin/env python3
# classAndObjects.py

# Super classe
class Animal: 

    def live(self):
        return "I am a living animal!"

# -----------------------------------

# Classe filha de Animal
class Human(Animal): 

    # definindo variaveis no construtor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return "My name is " + self.name + " and I have " + str(self.age) + " years!"

# -----------------------------------

# Classe filha de Animal
class Dog (Animal):
    # Class variable
    type = "Canine"

    # Constructor
    def __init__(self, name):
        self.name = name

    def bark (self):
        return self.name + ": Woof"
    
    # Funções precisam do self 
    def eat_food(self):
        return "Food eaten"
# -----------------------------------

# Usando a classe Animal
an = Animal()
print("Animal says: {}".format(an.live()))

# Usando a classe Human
hu = Human("Valmir", 21)
print("Human says: {}".format(hu.info()))
print("Human says: {}".format(hu.live()))

# Usando a classe DOG
Tobby = Dog("Tobby")

print("The name of my Dog is: {}".format(Tobby.name))
print("Tipo: {}".format(Tobby.type))
print(Tobby.eat_food())
print(Tobby.bark())



# ----------------------------------- Sobre escrevendo metodos
class Person:

    def __init__(self, name, age): # Custom crustuctor
        self.name = name
        self.age = age

    # overload "=="
    def __eq__(self, other):
        return self.name == other.name and \
                self.age == other.age

    # overload "!="
    def __ne__(self, other):
        return not self == other

    # overload ">"
    def __gt__(self, other):
        return self.age > other.age

    # overload like to string in JAVA
    def __str__(self):
        return self.name + "is " + str(self.age) + " years old!"

# utilizando os metodos 

a = Person("João", 32)  
b = Person("Henrique", 45)

print(a == b) # false
print(a != b) # true
print(a > b)  # false
print(a < b)  # true
print(str(b)) 
print(str(a))
