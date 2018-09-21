# Tratamento de ERROS
def ask():
    # Ler dados da entrada padrão
    numberStr = input("What is your favorite number?\n")

    # tratar erros
    try:
        number = int(numberStr) # transforma em inteiro
    except ValueError:
        number = None

    print("Your favorite is " + str(numberStr))

# Chamda da função
ask()

