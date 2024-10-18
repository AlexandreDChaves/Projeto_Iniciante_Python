import random

usuario = input("Pedra,papel ou tesoura? ").lower()
opcoes = 'pedra', 'papel', 'tesoura'
pc = random.choice(opcoes)
if ((usuario == 'pedra' and pc == 'tesoura') or 
(usuario == 'papel' and pc == 'pedra') or
(usuario == 'tesoura' and pc == 'papel')):
    print("Você ganha!")
    print(f"Computador escolheu: {pc}")
elif usuario == pc:
    print("Empate")
else:
    print("Você perde!")
    print(f"Computador escolheu: {pc}")