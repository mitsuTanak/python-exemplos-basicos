# Repetir código
while True:
    # Tabuada

    print(" ")
    num = int(input("Informe um numero: "))
    print("")
    print(f"Tabuada do {num}")
    print("")



    # Laço 'for'
    for i in range (1, 11):
        # calcula tabuada
        result = num * i

        # exibe 'Numero Escolhido * Numero do laço for = calculo da tabuada
        print(f"{num} * {i} = {result}")

        # Avança o numero
        i+=1
    
    # Pergunta se quer Repetir
    continuar = input("\n Deseja calcular de novo? (s/n): ")

    # caondicional de repetição
    if continuar.lower() != 's':
        print("Calculo encerrado!")
        # para código
        break
