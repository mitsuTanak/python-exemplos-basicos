#variaveis
nome = input("Informe seu nome: ")
idade = int(input("Informe sua Idade: "))

#verifica idade
if idade >= 18:
    print(f"Olá, {nome}! Você tem {idade}, logo você é maior de idade!")
else:
    print(f"Olá, {nome}! Você tem {idade}, logo você é menor de idade!")