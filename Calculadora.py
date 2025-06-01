import tkinter as tk

# Cores do tema escuro
COR_FUNDO = "#1e1e1e"
COR_BOTAO = "#333333"
COR_TEXTO = "#ffffff"
COR_ENTRADA = "#2a2a2a"

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
            entrada.after(1000, lambda: entrada.delete(0, tk.END))  # Limpa após 1 segundo
    elif botao == "C":
        entrada.delete(0, tk.END)
    elif botao == "DEL":
        entrada.delete(len(expressao)-1, tk.END)
    else:
        entrada.insert(tk.END, botao)

def tecla_pressionada(event):
    tecla = event.keysym

    if tecla in "0123456789":
        clicar(tecla)
    elif tecla == "plus" or event.char == "+":
        clicar("+")
    elif tecla == "minus" or event.char == "-":
        clicar("-")
    elif tecla == "asterisk" or event.char == "*":
        clicar("*")
    elif tecla == "slash" or event.char == "/":
        clicar("/")
    elif tecla == "Return":
        clicar("=")
    elif tecla == "BackSpace":
        clicar("DEL")
    elif tecla == "Escape":
        clicar("C")
    elif tecla in ["period", "comma", "KP_Decimal", "."]:
        clicar(".")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, width=16, font=('Arial', 24), borderwidth=0, relief="flat",
                   bg=COR_ENTRADA, fg=COR_TEXTO, insertbackground=COR_TEXTO)
entrada.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Botões da calculadora
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', 'DEL', '+',
    '='
]

# Criar os botões
row = 1
col = 0
for botao in botoes:
    comando = lambda x=botao: clicar(x)
    tk.Button(janela, text=botao, width=5, height=2, font=('Arial', 18),
              bg=COR_BOTAO, fg=COR_TEXTO, activebackground="#555555", activeforeground="#ffffff",
              relief="flat", command=comando).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Ativar suporte ao teclado
janela.bind("<Key>", tecla_pressionada)

# Iniciar a calculadora
janela.mainloop()
