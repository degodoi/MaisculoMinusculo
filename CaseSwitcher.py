import tkinter as tk
import pyperclip  # Biblioteca para manipular a área de transferência

def converter_texto():
    texto_entrada = entrada_texto.get("1.0", tk.END).strip()  # Obter o texto da caixa de texto
    if texto_entrada.islower():
        texto_convertido = texto_entrada.upper()
    else:
        texto_convertido = texto_entrada.lower()
    resultado.config(text=texto_convertido)

def copiar_texto():
    texto_copiado = resultado.cget("text")
    pyperclip.copy(texto_copiado)  # Usar pyperclip para copiar o texto
    # Informar ao usuário que o texto foi copiado
    label_status.config(text="Texto copiado para a área de transferência!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Conversor de Texto @degodoi.felipe")
janela.geometry("500x300")  # Ajuste do tamanho da janela

# Componentes da interface gráfica
rotulo_instrucao = tk.Label(janela, text="Digite o texto:", font=("Arial", 12))
rotulo_instrucao.pack()

entrada_texto = tk.Text(janela, height=5, width=60)  # Ajuste da caixa de texto
entrada_texto.pack()

botao_converter = tk.Button(janela, text="Converter", command=converter_texto)
botao_converter.pack()

resultado = tk.Label(janela, text="", font=("Arial", 12), wraplength=450, justify=tk.LEFT)  # Ajuste do rótulo de resultado
resultado.pack()

botao_copiar = tk.Button(janela, text="Copiar", command=copiar_texto)
botao_copiar.pack()

label_status = tk.Label(janela, text="", fg="green")
label_status.pack()

# Iniciar a janela
janela.mainloop()
