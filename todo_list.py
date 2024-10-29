tarefas= []

def add_tarefa(tarefa):
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def remove_tarefa(tarefa):
    if tarefa in tarefas:
        tarefas.remove(tarefa)
        print("tarefa removida com sucesso!")
    else:
        print("Tarefa não localizada")

def display_tarefa():
    if tarefas:
        print("Todo list: ")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")
    else:
        print("Todo list vazia")

def tarefa_usuario():
    return input("Digite a terefa: ")

def remover_tarefa_usuario():
    return input("Digite a terefa para remover: ")

def escolha_tarefa():
    return input("Digite a para adicionar, r para remover, d visualizar tarefa, s para sair: ").lower()

def main():
    while True:
        escolha = escolha_tarefa()
        if escolha == 'a':
            tarefa = tarefa_usuario()
            add_tarefa(tarefa)
        elif escolha == 'r':
            tarefa = remover_tarefa_usuario()
            remove_tarefa(tarefa)
        elif escolha == 'd':
            display_tarefa(tarefas)
        elif escolha == 's':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

'''add_tarefa("acordar cedo")
add_tarefa("codar constantimente")
display_tarefa(tarefas)
remove_tarefa("acordar cedo")
display_tarefa(tarefas)'''