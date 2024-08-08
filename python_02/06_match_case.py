opcao = int(input("Indique a opção desejda: "))

#seleção de opção

match opcao:
    case 1:
        print("Suporte Tecnico")
    case 2:
        print("Financeiro")
    case 3:
        print("Nossos Produtos")
    case 4:
        print("Outros assuntos")
    case 5:
        print("Opção invalida!")