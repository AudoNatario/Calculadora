import tkinter as tk

def clicar(botao):
    expressao = entrada.get()
    if botao == "=":
        try:
            resultado = str(eval(expressao))
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    elif botao == "DEL":
        entrada.delete(len(expressao)-1, tk.END)
    else:
        entrada.insert(tk.END, botao)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Campo de entrada
entrada = tk.Entry(janela, width=16, font=('Arial', 24), borderwidth=2, relief="ridge")
entrada.grid(row=0, column=0, columnspan=4)

# Lista de botões incluindo o DEL
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', 'DEL', '+',
    '='
]

# Criar botões na interface
row = 1
col = 0
for botao in botoes:
    comando = lambda x=botao: clicar(x)
    tk.Button(janela, text=botao, width=4, height=2, font=('Arial', 18), command=comando).grid(row=row, column=col)
    col += 1
    # Ajusta as linhas para o botão "=" ficar sozinho na última linha
    if col > 3:
        col = 0
        row += 1

janela.mainloop()
