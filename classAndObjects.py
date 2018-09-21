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
