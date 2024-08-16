import time

i=1
while i<=3:
    user = input("Informe o Usuário: ")
    password = input("Informe a Senha: ")

    # Checagem
    if user != "Andréia" or password != "Quer0Ser0uvida":
        print("Usuário ou Senha incorreto!")
        print(" ")
        i+=1

        if i>=4:
            print("Tente nova mente em 30 segundos...")
            time.sleep(30)
    else:
        print(" ")
        print(f"Bem-Vindo, {user}")
        break

else:
    print(f"Você tentou {i}, aguarde para tentar de novo")

