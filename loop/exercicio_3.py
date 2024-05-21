quantidade = 3
nome = input(f"Digite seu nome :")
while quantidade>0:
    print(f"Voce ainda possui {quantidade} tentativas")
    senha=int(input("Digite a sua senha: "))
    if senha!=123456: 
        print("Senha incorreta!")
        quantidade-=1
    else:
        print("Senha Correta")
        print(f"Olá, {nome}. Seja bem-vindo ao nosso banco!")
        break
    if quantidade ==0:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um dos nossos caixas")