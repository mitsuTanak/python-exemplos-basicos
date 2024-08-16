# Importe, biblioteca de aparencia
import tkinter as tk

# Função para transferir texto do input para 'label'
def motrar_mensagem(): # def = define 

    texto = caixa_texto.get() # Obter o texto da caixa de texto
    label_resultado.config(text=texto) #Atualiza o texto da 'Label'

# Janela Principal
janela = tk.Tk() #importa o 'Tk' do 'tkinter'(apelidado: 'tk')

# Caracteristicas da Janela
janela.geometry("400x400") # tamanho da janela
janela.title("Exemplos de Interface") # titulo da janela (fica na bordinha)

# Criar uma caixa de texto para a entrada
caixa_texto = tk.Entry(janela, width=60) # chama a caixa de texto e define o tamanho
caixa_texto.pack(pady=10) # paddind y(eixo vertical)

# Criar um botão
botao = tk.Button(janela, text="Mostrar texto", command=motrar_mensagem) # chama o botão e define a função
botao.pack(pady=5) # paddind y(eixo vertical)

# Criar rotulo para mostrar o resultado 'label'
label_resultado = tk.Label(janela, text=" ") # labem em branco (vai ser substituida)
label_resultado.pack(pady=5) # paddind y(eixo vertical)


# Executa a janela
janela.mainloop() 