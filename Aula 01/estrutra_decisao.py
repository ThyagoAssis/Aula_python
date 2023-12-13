''' Estrutura de decisão
        Operadores lógicos
        <ul>
             == Verifica se possuem mesmo valor  </li>
             === Verifica se são identicas </li>
             != Verifica se são diferentes </li>
             < Verifica se é menor </li>
             > Verifica se é maior </li>
             <= Verifica se é menor igual
             >= Verifica se é maior igual


         Tipos de estrutura de decisão


            Estrura Simples
            Estruturas Compostas
            struturas encadeada
'''

print("Esutura simples - é dada por uma única decisão")

idade = 18
if idade >= 18:
    print("Maior de idade")

print("Estrutura composta - é dada por uma única decisão e uma saída padrão")
valor_um = 2
valor_dois = 3
if valor_um < valor_dois:
    print("Verdade")
else:
    print("Falso")

print("Estrutura encadeada - é dada por ter mais de uma decisão e uma saída padrão")

materia  = "Python"

if materia == "PHP":
    print("Linguagem de pragamação voltada para Web")
elif materia == "Java":
    print("Linguagem de programação Robusta")
elif (materia == "Python"):
    print("Linguagem de programação muito fácil de aprender")
else:
    print("Não conheço essa linguagem")