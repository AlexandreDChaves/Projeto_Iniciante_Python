pontos = 0
pergunta1 = input("Qual é a formula da água?\n a) AG\n b) PB\n c) H2O\n").lower()
resposta1 = 'c'
if pergunta1 == resposta1:
    print("Acertou!")
    pontos += 1
else:
    print("Errou!")
pergunta2 = input("Qual é a capital do Brasil?\n a) Bogotá\n b) Brasília\n c) Caracas\n").lower()
resposta2 = 'b'
if pergunta2 == resposta2:
    print("Acertou!")
    pontos += 1
else:
    print("Errou!")
print(f"Total de pontos: {pontos}")