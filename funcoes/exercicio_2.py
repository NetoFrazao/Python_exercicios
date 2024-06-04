def calcularMedia(nota1, nota2, nota3, nota4):
    media = (nota1+nota2+nota3+nota4)/4
    return media

def aprovacao(media):
    if m>=5:
        return "Voce foi aprovado"
    else:
        return "Voce foi reprovado"


print("Calculadora de Media")
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))
m = calcularMedia(n1,n2,n3,n4)
r = aprovacao(m)
print(f"Sua media é {m}. {r}")