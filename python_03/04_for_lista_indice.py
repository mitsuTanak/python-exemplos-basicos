# Lista usando o laço for
print("")
print("Lista de Lojas")
print("")

lojas = ["Santo André", "São Bernardo", "São Caetano do Sul", "Mauá", "Diadema"]

# Lista usando laço
for i, loja in enumerate(lojas, 1):
    print(f"{i}° - {loja}")