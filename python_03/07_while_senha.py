user = input("Informe o Usuário: ")
password = input("Informe a Senha: ")

# Checagem
if user != "Andréia" and password != "Quer0Ser0uvida":
    print("Usuário ou Senha incorreto!")
    print(" ")
else:
    print(f"Bem-Vindo, {user}")