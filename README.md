# Calculadora Python
[Calculadora](asset/calculadora.png)

## Passo a Passo
### 1. Importações e Configurações Iniciais

````Python
import customtkinter as calc
import re
````

* customtkinter: Uma biblioteca baseada no tkinter, mas com mais recursos visuais modernos. Usamos ela para criar a interface gráfica (GUI) da calculadora.
* *re: Módulo de expressões regulares, usado para manipular a entrada de texto da calculadora e tratar o símbolo de porcentagem.

### 2. Configuração do Tema e Criação da Janela
````Python
calc.set_appearance_mode('light')
app = calc.CTk()
app.title("Calculadora")
app.geometry("700x350")
app.maxsize(700, 350)
app.grid_columnconfigure((0, 1, 2, 3), weight=1)

````

* calc.set_appearance_mode('light'): Define o tema claro para a interface da calculadora.
* app = calc.CTk(): Cria a janela principal da aplicação.
* app.title(): Define o título da janela.
* app.geometry(): Define o tamanho da janela.
* app.maxsize(): Limita o redimensionamento da janela a 700x350 pixels.
* app.grid_columnconfigure(): Configura as colunas para que o conteúdo seja distribuído proporcionalmente, o que garante que a interface fique bem alinhada.

### 3. Variável Global para Armazenar a Expressão

````Python
expressao = ""
````
* Esta variável guarda a expressão matemática que o usuário insere, como 100+80%.

### 4. Função para Atualizar a Entrada de Texto

````code
def adicionar_valor(valor):
    global expressao
    expressao += str(valor)
    numero.delete(0, calc.END)
    numero.insert(calc.END, expressao)
````

* adicionar_valor(valor): Recebe o valor do botão clicado (um número ou operador).
* expressao += str(valor): O valor clicado é adicionado à expressão.
* numero.delete(0, calc.END): Limpa o campo de texto.
* numero.insert(calc.END, expressao): Atualiza o campo de texto com a nova expressão.

### 5. Função de Cálculo da Expressão

```` Python
def calcular():
    global expressao
    try:
        expressao_modificada = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)*100', expressao)
        resultado = str(eval(expressao_modificada))
        numero.delete(0, calc.END)
        numero.insert(calc.END, resultado)
        expressao = resultado
    except Exception as e:
        numero.delete(0, calc.END)
        numero.insert(calc.END, "Erro")
        expressao = ""
````

* calcular(): Processa a expressão inserida.
* expressao_modificada: Usa uma expressão regular para encontrar números seguidos de % e substitui por uma fração que representa a porcentagem. Exemplo: 80% é transformado em (80/100)*100.
* eval(): Avalia e executa a expressão matemática. Ele lida com operações como somar, subtrair, multiplicar, dividir e porcentagens.
* try/except: Tenta calcular a expressão e, se houver algum erro (como dividir por zero), exibe "Erro" no campo de texto.

### 6. Função para Limpar a Entrada

````Python
def limpar():
    global expressao
    expressao = ""
    numero.delete(0, calc.END)
````

* limpar(): Reseta a expressão e limpa o campo de texto, permitindo que o usuário comece de novo.

### 7. Criação da Caixa de Entrada

````Python
numero = calc.CTkEntry(app, placeholder_text="", font=("Arial", 24), justify="right")
numero.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)
````

* numero: Campo de entrada de texto onde a expressão e o resultado são exibidos.
* font=("Arial", 24): Define a fonte e o tamanho do texto na entrada.
* justify="right": Alinha o texto à direita, como em uma calculadora comum.

### 8. Criação dos Botões de Números e Operações

> Cada botão é criado com um comando associado. Aqui estão alguns exemplos:

#### Botão "7":
````Python
button7 = calc.CTkButton(app, text="7", fg_color='#046307', hover_color='#5c9f59', command=lambda: adicionar_valor(7))
button7.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
````

[Exemplo do Botão 7](asset/botao7.png)
  

