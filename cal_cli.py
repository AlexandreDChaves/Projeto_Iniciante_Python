import sys
if len(sys.argv) != 4:
    print("Exemplo de como utilizar a calculadora:\n python cal_cli.py numero numero operação")
    print("Operações válidas: somar, subtrair, multiplicar, divisao")
    sys.exit(1)

try:
    numero1 = int(sys.argv[1])
    numero2 = int(sys.argv[2])
except ValueError:
    print("Erro! ambos precisam ser numeros")

if sys.argv[3] == 'somar':
    resultado = numero1 + numero2
    print(f"A soma de {numero1} + {numero2} é: {resultado}")
elif sys.argv[3] == 'subtrair':
    resultado = numero1 - numero2
    print(f"A subtração de {numero1} - {numero2} é: {resultado}")
elif sys.argv[3] == 'multiplicar':
    resultado = numero1 * numero2
    print(f"A multiplicação de {numero1} x {numero2} é: {resultado}")
elif sys.argv[3] == 'divisao':
    if numero2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = numero1 // numero2
        print(f"A divisão de {numero1} / {numero2} é: {resultado}")
else:
    print("Erro: Operação inválida. Use uma das seguintes operações: somar, subtrair, multiplicar, divisao")