import tkinter as tk

def inverter_frase():
    frase = entrada.get()
    frase_invertida = frase[::-1]
    resultado_label.config(text=f"Frase invertida: {frase_invertida}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Inversor de Frases")

# Entrada de texto
entrada_label = tk.Label(janela, text="Digite uma frase:")
entrada_label.pack()

entrada = tk.Entry(janela, width=50)
entrada.pack()

# Botão para inverter a frase
botao_inverter = tk.Button(janela, text="Inverter", command=inverter_frase)
botao_inverter.pack()

# Label para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Inicia o loop da interface gráfica
janela.mainloop()