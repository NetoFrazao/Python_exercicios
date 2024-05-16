def calcularmedia(n, numeros):
    soma = sum(numeros)
    media = soma / n
    return media

def main():
    n = int(input("Digite a quantidade de notas que deseja: "))
    
    if n <= 0:
        print("Por favor, digite um número inteiro positivo.")
        return

    numeros = []
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    media = calcularmedia(n, numeros)
    print("A média aritmética dos números digitados é:", media)

if __name__ == "__main__":
       main()
