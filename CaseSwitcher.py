import tkinter as tk
import pyperclip  # Biblioteca para manipular a área de transferência

def converter_maiuscula():
    texto_entrada = entrada_texto.get("1.0", tk.END).strip()  # Obter o texto da caixa de texto
    texto_convertido = texto_entrada.upper()
    resultado.config(text=texto_convertido)
    atualizar_status("Texto convertido para maiúsculas.")

def converter_minuscula():
    texto_entrada = entrada_texto.get("1.0", tk.END).strip()  # Obter o texto da caixa de texto
    texto_convertido = texto_entrada.lower()
    resultado.config(text=texto_convertido)
    atualizar_status("Texto convertido para minúsculas.")

def copiar_texto():
    texto_copiado = resultado.cget("text")
    pyperclip.copy(texto_copiado)  # Usar pyperclip para copiar o texto
    atualizar_status("Texto copiado para a área de transferência.")

def atualizar_status(mensagem):
    label_status.config(text=mensagem)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Texto @degodoi.felipe")
janela.geometry("500x300")  # Ajuste do tamanho da janela

# Componentes da interface gráfica
rotulo_instrucao = tk.Label(janela, text="Digite o texto:", font=("Arial", 12))
rotulo_instrucao.pack()

entrada_texto = tk.Text(janela, height=5, width=60)  # Ajuste da caixa de texto
entrada_texto.pack()

# Frame para agrupar os botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Botões sem ícones
botao_maiuscula = tk.Button(frame_botoes, text="Maiúsculas", command=converter_maiuscula)
botao_maiuscula.pack(side=tk.LEFT, padx=10)

botao_minuscula = tk.Button(frame_botoes, text="Minúsculas", command=converter_minuscula)
botao_minuscula.pack(side=tk.LEFT, padx=10)

botao_copiar = tk.Button(frame_botoes, text="Copiar", command=copiar_texto)
botao_copiar.pack(side=tk.LEFT, padx=10)

# Rótulo para exibir o texto convertido
resultado = tk.Label(janela, text="", font=("Arial", 12), wraplength=450, justify=tk.LEFT)
resultado.pack()

# Rótulo de status
label_status = tk.Label(janela, text="", fg="green")
label_status.pack()

# Iniciar a janela
janela.mainloop()
