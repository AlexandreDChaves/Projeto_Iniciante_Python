print("POST IT IN PYTHON")
tarefa = input("Digite sua tarefa: ")
with open('bloco.txt', 'a') as arquivo:
    arquivo.write(tarefa + '\n')

with open('bloco.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)