senha = input("Digite a senha para avaliar a força da mesma criada: ")
tamanho_minimo = 13
contem_maiuscula = any(char.isupper() for char in senha)
contem_minuscula = any(char.islower() for char in senha)
contem_numero = any(char.isdigit() for char in senha)
contem_especial = any(not char.isalnum() for char in senha)
tamanho_senha = len(senha) >= tamanho_minimo

if contem_maiuscula and contem_minuscula and contem_numero and contem_especial and tamanho_senha:
    print("Senha forte")
elif (contem_maiuscula and contem_minuscula) or (contem_numero and contem_especial) or (tamanho_senha):
    print("Senha Média")
else:
    print("Senha Fraca")