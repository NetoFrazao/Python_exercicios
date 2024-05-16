n_pares = 0

print("Digite 5 números inteiros positivos: ")
for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        n_pares += 1

print("A quantidade de números pares é:", n_pares)