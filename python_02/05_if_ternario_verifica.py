valor = int(input("Informe o valor: "))

# uso if ternario
teste = "Situação normal." if valor<100 else "situação pré-diabetes" if valor in range (100, 125) else "Diabetes"

# Alerta
print(teste)