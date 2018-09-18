#! /usr/bin/env python3
# adivinha.py - Primeiro exemplo de módulo.

# Strings podem ser definas com aspas simples e duplas 
""" 
Solicita que o usuário adivinha qual a opção escolhida.
"""

# Importando da bibilioteca padrao
import random

palpite, tentativas = "", 0                             # atribuição de multiplas Variaveis
frutas = ["Pera", "Laranja", "Melancia", "Ameixa"]      # Vetor 
minha_preferida = random.choice(frutas).upper()         # Sorteia um elemento da lista
while (palpite != minha_preferida):                     # Loop condicional
    print(frutas)                                       # Printa o vetor completo
    palpite = input("Adivinhe minha fruta favorita: ")  # Solicita informação do usuário
    palpite = palpite.upper()                           # Converte as letras para maiusculas
    tentativas += 1
    if (palpite != minha_preferida):                    # Condicional
        print("Não é essa não, tente novamente!")       # saida padrão
print("Muito bem, voce acertou.\nNumero de tentativas = {}".format(tentativas))   # Formata o valor para concaternação na string
    