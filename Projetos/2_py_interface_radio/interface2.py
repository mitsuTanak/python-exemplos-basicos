import tkinter as tk
from tkinter import ttk

# Função para atualizar (nome e as escolhas)
def atualizar_resultados():
    # Obter nome de usuario
    nome = caixa_texto.get()

    # Obter preferencia de bebida
    preferencia = var_radio.get()

    # Verifica o tipo de saudação selecionada - Informal
    if var_check_saudacao.get():
        saudacao = "Olá"
    else:
        saudacao = "Bem-Vindo"

    #Formal
    if var_check_saudacao.get():
        saudacao = f"{saudacao}, caro(a)"

    # Obter cor favorita selecionada
    cor_favorita = combo_cor.get()

    # Montar mensagem final
    mensagem = f"{saudacao} {nome}! \n Você prefere {preferencia}. "
    if cor_favorita:
        mensagem += f"sua cor favorita é: {cor_favorita}."

    # Atualizar o texto
    label_resultado.config(text=mensagem)

# Função para limpar (nome e as escolhas)
def limpar_campo():
    caixa_texto.delete(0, tk.END)
    var_radio.set('café')
    var_check_saudacao.set(False)
    var_check_personalizado.set(False)
    combo_cor.set(" ")
    label_resultado.config(text="")

# Janela principal
janela = tk.Tk()
janela.title("Interface Avançada") # Titulo pagina
janela.geometry("400x500") # Tamanho da pagina

# Criar caixa entada
label_nome = tk.Label(janela, text= "Digite seu nome: ")
label_nome.pack(pady=5)# paddind y(eixo vertical)

caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)# paddind y(eixo vertical)

# Criar botões de radio
label_preferencia = tk.Label(janela, text= "Selecione sua Preferencia")
label_preferencia.pack(pady=5)# paddind y(eixo vertical)

var_radio = tk.StringVar(value='Café')# pré selecionadp

radio_cafe = tk.Radiobutton(janela, text="Café", variable=var_radio, value="Café") # Opção
radio_cha = tk.Radiobutton(janela, text="Chá", variable=var_radio, value="Chá") # Opção
radio_suco = tk.Radiobutton(janela, text="Suco ", variable=var_radio, value="Suco") # Opção
radio_agua = tk.Radiobutton(janela, text="Água", variable=var_radio, value="Água") # Opção

radio_cafe.pack()
radio_cha.pack()
radio_suco.pack()
radio_agua.pack()

# Criar caixas de seleção: "CheckBox"
var_check_saudacao = tk.BooleanVar()
check_saudacao = tk.Checkbutton(janela, text="Usar saudação informal", variable=var_check_saudacao)
check_saudacao.pack(pady=5)

var_check_personalizado = tk.BooleanVar()
check_personalizado = tk.Checkbutton(janela, text="Usar saudação personalizada", variable=var_check_personalizado)
check_personalizado.pack(pady=5)

# Lista de opcões 'comboBox'
label_cor = tk.Label(janela, text="Digite a sua cor favorita")
label_cor.pack(pady=5)
combo_cor = ttk.Combobox(janela, values=["Vermelho", "Verde", "Azul", "Verde", "Amarela", "Roxo"])
combo_cor.pack(pady=5)

# Criar botões
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_resultados)
botao_atualizar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campo)
botao_limpar.pack(pady=10)

# Criar um rotulo para mostrar o resultado "Label"
label_resultado = tk.Label(janela, text="", wraplength=350)
label_resultado.pack(pady=10)

# Executa a janela
janela.mainloop() 