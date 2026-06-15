# Calculadora com Interface Gráfica em Python 🧮
Este projeto é uma calculadora funcional desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. O diferencial deste projeto é que ele não utiliza a função nativa `eval()` do Python para resolver as contas mas sim, possui um algoritmo próprio de análise sintática para processar e calcular as expressões matemáticas.

## Funcionalidades
* **Interface Visual Própria:** Criada com Tkinter e contendo visor responsivo e disposição dos botões em grid.
* **Respeito à Precedência Matemática:** O motor de cálculo processa multiplicações (`*`) e divisões (`/`) antes de somas (`+`) e subtrações (`-`).
* **Tratamento de Erros:** Exibe uma mensagem de "ERRO" na tela se o usuário tentar realizar uma operação inválida, evitando o fechamento inesperável da aplicação.
* **Limpeza do Visor:** Botão `C` funcional para reiniciar a expressão atual.

## Tecnologias Utilizadas
* **Python 3.x**
* **Tkinter** (Biblioteca Python para interfaces gráficas)


## 💻 Como Executar o Projeto
Como o Tkinter já vem instalado por padrão no Python na maioria dos sistemas, basta rodar o arquivo principal.

1. Clone o repositório:
   bash
    git clone https://github.com/vanscopel/CALCULADORA-PYTHON.git

2. Acesse a pasta do projeto:
   bash
    cd CALCULADORA-PYTHON

3. Execute o script:
    python calculadora.py