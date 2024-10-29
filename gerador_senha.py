import random
import string

def gerar_senha(comprimento):
    
    if comprimento < 4:
        print("A senha deve ter pelo menos 4 caracteres para atender aos critérios de segurança.")
        return None
    
    
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    caracteres_especiais = string.punctuation

    
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(digitos),
        random.choice(caracteres_especiais)
    ]

    
    todos_caracteres = letras_maiusculas + letras_minusculas + digitos + caracteres_especiais
    
    for _ in range(comprimento - 4):
        senha.append(random.choice(todos_caracteres))

    random.shuffle(senha)

    senha_final = ''.join(senha)
    return senha_final


comprimento = int(input("Digite o comprimento desejado para a senha (mínimo 4): "))
senha_gerada = gerar_senha(comprimento)
if senha_gerada:
    print(f"Senha gerada: {senha_gerada}")
