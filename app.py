import customtkinter as calc
import re

# Configuração do modo claro
calc.set_appearance_mode('light')

# Janela principal da aplicação
app = calc.CTk()
app.title("Calculadora")
app.geometry("700x350")
app.maxsize(700, 350)

# Configurando as colunas para ter distribuição proporcional
app.grid_columnconfigure((0, 1, 2, 3), weight=1)

# Variável global para armazenar a expressão
expressao = ""

# Função para atualizar a entrada de texto
def adicionar_valor(valor):
    global expressao
    expressao += str(valor)
    numero.delete(0, calc.END)
    numero.insert(calc.END, expressao)

# Função para calcular o resultado
def calcular():
    global expressao
    try:
        # Substitui expressões do tipo "80%" por "80/100"
        # Substitui expressões do tipo "valor + n%" por "valor + (n/100) * valor"
        expressao_modificada = re.sub(r'(\d+(\.\d+)?)(\s*\+\s*)(\d+(\.\d+)?)(%)', 
                                       lambda m: f'{m.group(1)} + ({m.group(4)} / 100) * {m.group(1)}', 
                                       expressao)
        # Substitui expressões do tipo "valor - n%" por "valor - (n/100) * valor"
        expressao_modificada = re.sub(r'(\d+(\.\d+)?)(\s*-\s*)(\d+(\.\d+)?)(%)', 
                                       lambda m: f'{m.group(1)} - ({m.group(4)} / 100) * {m.group(1)}', 
                                       expressao_modificada)
        resultado = str(eval(expressao_modificada))  # Avalia a expressão matemática
        numero.delete(0, calc.END)        # Limpa a entrada
        numero.insert(calc.END, resultado) # Exibe o resultado
        expressao = resultado             # Atualiza a expressão com o resultado
    except Exception as e:
        numero.delete(0, calc.END)
        numero.insert(calc.END, "Erro")
        expressao = ""

# Função para limpar a entrada
def limpar():
    global expressao
    expressao = ""
    numero.delete(0, calc.END)

# Linha 0 - Entrada de texto para mostrar os números e o resultado
numero = calc.CTkEntry(app, placeholder_text="", font=("Arial", 24), justify="right")
numero.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

# Linha 2 - Botões 7, 8, 9 e multiplicação (*)
button7 = calc.CTkButton(app, text="7", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(7))
button7.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")

button8 = calc.CTkButton(app, text="8", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(8))
button8.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

button9 = calc.CTkButton(app, text="9", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(9))
button9.grid(row=2, column=2, padx=20, pady=(0, 20), sticky="w")

buttonMulti = calc.CTkButton(app, text="*", fg_color='#00008b', hover_color='#000', command=lambda: adicionar_valor("*"))
buttonMulti.grid(row=2, column=3, padx=20, pady=(0, 20), sticky="w")

# Linha 3 - Botões 4, 5, 6 e divisão (/)
button4 = calc.CTkButton(app, text="4", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(4))
button4.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")

button5 = calc.CTkButton(app, text="5", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(5))
button5.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w")

button6 = calc.CTkButton(app, text="6", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(6))
button6.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")

buttonDiv = calc.CTkButton(app, text="/", fg_color='#00008b', hover_color='#000', command=lambda: adicionar_valor("/"))
buttonDiv.grid(row=3, column=3, padx=20, pady=(0, 20), sticky="w")

# Linha 4 - Botões 1, 2, 3 e subtração (-)
button1 = calc.CTkButton(app, text="1", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(1))
button1.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="w")

button2 = calc.CTkButton(app, text="2", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(2))
button2.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")

button3 = calc.CTkButton(app, text="3", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(3))
button3.grid(row=4, column=2, padx=20, pady=(0, 20), sticky="w")

buttonSub = calc.CTkButton(app, text="-", fg_color='#00008b', hover_color='#000', command=lambda: adicionar_valor("-"))
buttonSub.grid(row=4, column=3, padx=20, pady=(0, 20), sticky="w")

# Linha 5 - Botões %, 0, ponto (.) e adição (+)
buttonP = calc.CTkButton(app, text="%", fg_color='#00008b', hover_color='#000', command=lambda: adicionar_valor("%"))
buttonP.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew", columnspan=1)

button0 = calc.CTkButton(app, text="0", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(0))
button0.grid(row=5, column=1, padx=20, pady=(0, 20), sticky="ew", columnspan=1)

buttonDot = calc.CTkButton(app, text=".", fg_color='#00008b', hover_color='#000', command=lambda: adicionar_valor("."))
buttonDot.grid(row=5, column=2, padx=20, pady=(0, 20), sticky="w")

buttonAdd = calc.CTkButton(app, text="+", fg_color='#00008b', hover_color='#000', command=lambda: adicionar_valor("+"))
buttonAdd.grid(row=5, column=3, padx=20, pady=(0, 20), sticky="w")

# Linha 6 - Botão de igual (=) e limpar (C)
buttonClear = calc.CTkButton(app, text="C", fg_color='#e80700', hover_color='#831106', command=limpar, height=30)
buttonClear.grid(row=6, column=0, padx=20, pady=0, sticky="ew", columnspan=2)

buttonEqual = calc.CTkButton(app, text="=", fg_color='#e80700', hover_color='#831106', command=calcular, height=30)
buttonEqual.grid(row=6, column=2, padx=20, pady=0, sticky="ew", columnspan=2)

# Executar o loop da aplicação
app.mainloop()
