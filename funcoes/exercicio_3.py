def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def aprovacao(media):
    if media >= 5:
        return f"Aprovado com média {media:.2f}"
    else:
        return f"Reprovado com média {media:.2f}"

nome_aluno = input("Digite o nome do aluno: ")

notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)


media = calcular_media(notas)

resultado = aprovacao(media)

print(f"O aluno {nome_aluno} está {resultado}")