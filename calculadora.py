numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Não é possível dividir por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print("O resultado é:", resultado)