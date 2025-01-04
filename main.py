from datetime import datetime

def main():
    tarefas = []

    while True:
        print("\n===== Lista de Tarefas =====")
        print("1. Adicionar Tarefa")
        print("2. Mostrar Tarefas")
        print("3. Mostrar Tarefas por Data")
        print("4. Marcar Tarefa como Concluída")
        print("5. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            n_tarefas = int(input("Quantas tarefas você quer adicionar?: "))
            for i in range(n_tarefas):
                tarefa = input("Digite a tarefa: ")
                data = input("Digite a data de vencimento (formato DD/MM/AAAA): ")
                try:
                    data_formatada = datetime.strptime(data, "%d/%m/%Y").date()
                    tarefas.append({"Tarefa": tarefa, "Concluída": False, "Data": data_formatada})
                    print("Tarefa Adicionada!")
                except ValueError:
                    print("Data inválida. Use o formato DD/MM/AAAA.")

        elif escolha == '2':
            print("\n===== Todas as Tarefas =====")
            for index, tarefa in enumerate(tarefas):
                status = "Concluída" if tarefa["Concluída"] else "Não Concluída"
                print(f"{index + 1}. {tarefa['Tarefa']} - {status} - Vencimento: {tarefa['Data']}")

        elif escolha == '3':
            data_filtro = input("Digite a data para filtrar (formato DD/MM/AAAA): ")
            try:
                data_formatada = datetime.strptime(data_filtro, "%d/%m/%Y").date()
                print(f"\n===== Tarefas para {data_formatada} =====")
                tarefas_encontradas = [t for t in tarefas if t["Data"] == data_formatada]
                if tarefas_encontradas:
                    for index, tarefa in enumerate(tarefas_encontradas):
                        status = "Concluída" if tarefa["Concluída"] else "Não Concluída"
                        print(f"{index + 1}. {tarefa['Tarefa']} - {status}")
                else:
                    print("Nenhuma tarefa encontrada para esta data.")
            except ValueError:
                print("Data inválida. Use o formato DD/MM/AAAA.")

        elif escolha == '4':
            tarefa_index = int(input("Escreva o número da tarefa para marcá-la como concluída: ")) - 1
            if 0 <= tarefa_index < len(tarefas):
                tarefas[tarefa_index]["Concluída"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Número de tarefa inválido.")

        elif escolha == '5':
            print("Saindo da Lista de Tarefas.")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")


main()
