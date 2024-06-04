from tabulate import tabulate

def cadastrar_notas(alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    total_notas = 0
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno {nome}: "))
        notas.append(nota)
        total_notas += nota
    alunos[nome] = notas, total_notas

def calcular_media(total_notas):
    return total_notas / 4

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def mostrar_notas_cadastradas(alunos):
    table_data = []
    for aluno, (notas, total_notas) in alunos.items():
        media = calcular_media(total_notas)
        situacao = verificar_situacao(media)
        table_data.append([aluno, notas, f"{media:.2f}", situacao])

    print(tabulate(table_data, headers=["Aluno", "Notas", "Média", "Situação"], tablefmt="grid"))

alunos = {}
while True:
    print("\nMenu:")
    print("1. Cadastrar notas de um aluno")
    print("2. Mostrar notas cadastradas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_notas(alunos)
    elif opcao == "2":
        mostrar_notas_cadastradas(alunos)
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")