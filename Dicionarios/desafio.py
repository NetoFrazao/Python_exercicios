produtos = {}
num_itens = int(input(f"Quantos itens deseja:"))

for i in range(num_itens):
    nome = input(f"Digite o nome do produto {i+1}: ")
    valor = float(input(f"Digite o preço do produto {i+1}: "))
    qtd = int(input(f"Digite a quantidade {i+1}: "))
    produtos[i] = [nome, valor, qtd]

total = 0

print(50 * '-')
print('Carrinho de Compras')
print(50 * '-')

for cod, prod in produtos.items():
    subtotal = prod[1] * prod[2]
    print(f"{prod[0]} - R$ {prod[1]:.2f} - {prod[2]} un - R$ {subtotal:.2f}")
    total += subtotal

print(50 * '-')
print(f'Total de Compras: R$ {total:.2f}')
print(50 * '-')

