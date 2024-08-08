sabor = int(input("Indique o sabor desejado: "))

#seleção de opção
def sabor_pizza(sabor):
    match sabor:
        case 1:
            return print("Mussarela")
        
        case 2:
            return print("Calabresa")
        
        case 3:
            return print("Frango c/ Catupiry")
        
        case 4:
            return print("Portuguesa")
        
        case _:
            return print("Sabor")


sabor_pizza(sabor)