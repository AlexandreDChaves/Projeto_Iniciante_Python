opcao = float(input("Digite o valor para conversão: "))
moeda = input("Escolha a moeda (real, dolar ou euro): ").lower()
converter = input("Converter para (real, dolar ou euro): ").lower()

taxa_dolar_para_real = 5.68
taxa_real_para_dolar = 0.18
taxa_real_para_euro = 0.16
taxa_euro_para_real = 6.17
taxa_dolar_para_euro = 0.92
taxa_euro_para_dolar = 1.09

if moeda == 'dolar' and converter == 'real':
    resultado = opcao * taxa_dolar_para_real
    print(f"{opcao} dólares equivalem a {resultado:.2f} reais")
elif moeda == 'real' and converter == 'dolar':
    resultado = opcao * taxa_real_para_dolar
    print(f"{opcao} reais equivalem a {resultado:.2f} dólares")
elif moeda == 'real' and converter == 'euro':
    resultado = opcao * taxa_real_para_euro
    print(f"{opcao} reais equivalem a {resultado:.2f} euros")
elif moeda == 'euro' and converter == 'real':
    resultado = opcao * taxa_euro_para_real
    print(f"{opcao} euros equivalem a {resultado:.2f} reais")
elif moeda == 'dolar' and converter == 'euro':
    resultado = opcao * taxa_dolar_para_euro
    print(f"{opcao} dólares equivalem a {resultado:.2f} euros")
elif moeda == 'euro' and converter == 'dolar':
    resultado = opcao * taxa_euro_para_dolar
    print(f"{opcao} euros equivalem a {resultado:.2f} dólares")
else:
    print("Moeda ou conversão não cadastrada.")
