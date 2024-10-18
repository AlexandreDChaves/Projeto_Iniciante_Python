import random
contador_jogadas = 0
while True:
    pergunta = input("Gostaria de continuar jogando? s/n ").lower()
    if pergunta == 's':
        a = random.randint(1,6)
        b = random.randint(1,6)
        contador_jogadas += 1
        print(f"{a,b}")
    elif pergunta == 'n':
        print(f"Numero de jogadas: {contador_jogadas}")
        break
    else: 
        print("Jogada inválida")