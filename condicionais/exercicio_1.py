import json
import urllib.request

# Solicitar ao usuário o CEP
cep = input("Digite o CEP: ")

# Conatruir na URL de consulta
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # Fazer a requisição
    response = urllib.request.urlopen(url)

    # Ler o conteúdo da resposta
    data = response.read().decode("utf-8")

    #Converter JSON em dicionário Pythin
    endereco = json.loads(data)

    # Verificar se a consulta foi bem-sucedida
    if endereco.get("erro"):
        print("CEP não encontrado")
    else:
        # Armazenar informaçoes em variáveis
        logradouro = endereco["logradouro"] 
        complemento = endereco["complemento"] 
        bairro = endereco["bairro"]  
        cidade = endereco["localidade"]
        estado = endereco["uf"]

        #Exibir informações do endereço na tela
        print(f"Logradouro: {logradouro}")
        print(f"Complemento: {complemento}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")
    
    #Fechar a conexão
except Exception as e:
    print(f"Erro: {e}")