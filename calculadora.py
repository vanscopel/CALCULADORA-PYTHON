import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("600x700")

expressao = ""

#funcoes---------------------------------------------------------
def clicar(valor):
    global expressao
    expressao += str(valor)

    visor.delete(0, tk.END)
    visor.insert(tk.END, expressao)

def calcular():
    global expressao
    try:
        resultado= calcular_expressao(expressao)
        visor.delete(0, tk.END)
        visor.insert(tk.END, str(resultado))
        expressao= str(resultado)
    except:
        visor.delete(0, tk.END)
        visor.insert(tk.END,"Erro")
        expressao=""

def calcular_expressao(expr):
    numeros = []
    operadores = []

    numero_atual = ""

    for char in expr:
        if char.isdigit() or char ==".":
            numero_atual += char
        else:
            if numero_atual != "":
                numeros.append(float(numero_atual))
                numero_atual= ""
            if char in "+-*/" :
                operadores.append(char)

    if numero_atual != "":                    
        numeros.append(float(numero_atual))

    if not numeros:
        return 0


    i = 0
    while i < len(operadores):
        if operadores[i] == "*":
            numeros[i] = numeros [i] * numeros[i+1]
            del numeros[i+1]
            del operadores[i]
        elif operadores[i] == "/":
            numeros[i] = numeros[i] / numeros[i+1]
            del numeros[i+1]
            del operadores[i]
        else:
            i += 1

    resultado = numeros[0]
    for i, op in enumerate(operadores):
        if op =="+":
            resultado += numeros [i+1]
        elif op =="-":
            resultado -= numeros[i+1]

    return resultado

def limpar():
    global expressao
    expressao= ""
    visor.delete(0, tk.END)


#visor-----------------------------------------------------------
visor = tk.Entry(janela, font=("Courier New", 38), justify="right")
visor.grid(row=0, column=0, columnspan=4,sticky="nsew", pady=10)

#botoes----------------------------------------------------------
botoes = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
    ]

#---------------------------------------------------------------
linha = 1
coluna = 0

for botao in botoes:
    def comando(x=botao):
        if x =="=":
            return calcular
        elif x == "C":
            return limpar
        else:
            return lambda: clicar(x)
        
    btn = tk.Button(
        janela,
        text=botao,
        font=("Arial", 18),
        width=5,
        height=2,
        command=comando()
    )

    btn.grid(row=linha, column=coluna, sticky="nsew")

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha +=1

#--------------------------------------------------------------
for i in range(5):
    janela.rowconfigure(i, weight=1)
    janela.columnconfigure(i, weight=2)

janela.mainloop()