print("=====LOJAS=====")
print("")

#Array
lojas = ["Santo André", "São Bernardo", "São Caetano", "Diadema"]

# Laço For para exibir
for i, loja in enumerate(lojas, 1):
    print(f"{i} - {loja}")
    print("")

#Escolhendo uma loja para exibição
loja_selecionada = int(input("Selecione a loja desejada: "))

# #Exibindo a loja selecionada
# if 1<= loja_selecionada <= len(lojas):
#     print(lojas[loja_selecionada -1])
# else:
#     print("loja invaida")

# outra forma de exibir a loja selecionada
for i, lojas in enumerate(lojas, 1):
    if loja_selecionada == i:
        print(loja)
        break
else: 
    print("Loja invalida")