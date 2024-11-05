conta = 5
while True:
    try:
        opcao = int(input("Digite 1 para deposito e 2 para saque 3 para encerrar: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    if opcao == 1:
        valor = float(input("Digite o valor para deposito: "))
        if valor > 0:
            conta += valor
            print(f"Saldo total da conta: {conta}")
        else:
            print("Não é possível realizar o depósito menor que 0 ou igual.")
    elif opcao == 2:
        valor = float(input("Digite o valor para saque: "))
        if valor <= conta:
            conta-= valor
            print(f"Saldo atualizado da conta: {conta}")
        else:
            print("Saldo insuficiente")
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")