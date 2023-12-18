'''
1. O que são Funções?
As funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar o código e facilitam a manutenção.
'''

""" 2. Sintaxe Básica: """
def nome_da_funcao ():
    #corpo da função
    #---
    return resultado

""" 1 - def: Palavra-chave para definir uma função.
2 - nome_da_funcao: Identificador da função.
3 - parametro1, parametro2, ...: Parâmetros (opcionais) que a função pode receber.
4 - return resultado: Especifica o valor retornado pela função (opcional) """

print("Exemplo de Função Simples")
def saudacao():
    print("Ola mundo")

saudacao()

""" 4. Parâmetros e Argumentos:
Parâmetros: Variáveis na definição da função.
Argumentos: Valores passados durante a chamada da função. """
print("Função com parametros")

def cumprimento(nome):
    print("Bom dia: {}".format(nome))
    
cumprimento("Marcos")

print("Funções com Retorno:")

def soma(a, b):
    """Esta função retorna a soma de dois números."""
    resultado = a + b
    return resultado

# Chamando a função e armazenando o resultado
resultado_soma = soma(3, 5)
print("A soma é:", resultado_soma)

""" 6. Funções Integradas:
Python possui diversas funções integradas, como len(), print(), input(), entre outras. """

print("Funções Integradas:")

tamanho = len("Python")
print("O tamanho da string é:", tamanho)

""" 7. Escopo de Variáveis:
Variáveis Locais: Definidas dentro da função, acessíveis apenas dentro dela.
Variáveis Globais: Definidas fora da função, acessíveis em todo o programa. """
msg = "Sou uma varivel global"

def variaveis():
    global msg
    local = "Sou uma variável local"
    print(msg, " ", local)

variaveis()

""" 8. Funções Personalizadas: """

print("Funções Personalizadas:")

def calculo_potencia(base, expoente=2):
    """Calcula a potência de um número."""
    resultado = base ** expoente
    return resultado

# Chamando a função com argumento padrão
res1 = calculo_potencia(3)
print("3 elevado à 2ª potência é:", res1)

# Chamando a função com argumento personalizado
res2 = calculo_potencia(3, 4)
print("3 elevado à 4ª potência é:", res2)


""" 9. Conclusão:
Funções tornam o código modular e mais fácil de entender.
Parâmetros e argumentos são fundamentais para a flexibilidade das funções.
O retorno é opcional, mas essencial quando a função precisa produzir um resultado.
 """
 
"""  outro exemplos """

# Função de Soma
def soma(a, b):
    return a + b

# Função de Multiplicação
def multiplicacao(a, b):
    return a * b

# Testando as funções
resultado_soma = soma(3, 5)
resultado_multiplicacao = multiplicacao(4, 6)

print("Resultado da Soma:", resultado_soma)
print("Resultado da Multiplicação:", resultado_multiplicacao)


