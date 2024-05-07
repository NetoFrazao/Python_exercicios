def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

area = calcular_area_triangulo(base, altura)

print("A área do triângulo é:",area)