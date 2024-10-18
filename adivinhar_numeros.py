import random
numero = random.randint(1,100)

while True:
    try:
        pergunta = int(input("Adivinhe um numero entre 1 e 100: "))

        if pergunta < numero:
            print("Muito baixo")
        elif pergunta > numero:
            print("Muito alto")
        else:
            print("Voce acertou o numero")
            break
    except ValueError:
        print("Digite um numero válido")