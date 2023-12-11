'''

<h1> Estruturas de Repetição </h1>
        <p>Estruras de repetição serve para executar uma operação inúmeras vezes</p>

        <h2> Estruturas mais usadas em PHP</h2>
        <ul>
            <li> while </li>
            <li> for </li>


'''

'''
O while é uma estrutura de repetição utilizada quando queremos que determinado bloco de código seja executado ENQUANTO (do inglês while) determinada condição for satisfeita.
Em outras palavras: só saia da estrutura de repetição quando a condição não for mais satisfeita.
Sua sintaxe básica é:
'''
print("Loop com while")
contador = 0

while contador < 10:
    print(f'Valor do contador é {contador}')
    contador += 1

print("While com else")
contador = 0

while contador < 10:
    contador += 1
    print(f'Valor do contador é {contador}')
else:
    print(f'Fim do while e o valor do contador é {contador}')


'''
O for é utilizado para percorrer ou iterar sobre uma sequência de dados (seja esse uma lista, uma tupla, uma string), executando um conjunto de instruções em cada item.
'''


print("Primeiro for")

lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)

print("For com else")

sequencia = [1,2,3]
for item in sequencia:
    print(item)
else:
    print('Todos os items foram exibidos com sucesso')

print("Outro exemplo do for")
computador = ['Processador', 'Teclado', 'Mouse']

for item in computador:
    print(item)


print("Form com chave valor")
notas = {
    'Potuguês': 7,
    'Matemática': 9,
    'Lógica': 7,
    'Algoritmo': 7
}

for chave in notas.items():
    print("{}: ".format(chave))


for chave, valor in notas.items():
    print(f"{chave}: {valor}")