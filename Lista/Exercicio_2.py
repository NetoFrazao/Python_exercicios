numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
print("Lista de números:", numeros)

soma_numeros = sum(numeros)
menor_numeros = min(numeros)
maior_numeros = max(numeros)
media = soma_numeros/len(numeros)

print("Soma dos números:", soma_numeros)
print("Maior número:", maior_numeros)
print("Menor número:", menor_numeros)
print("Média dos números:", media)