'''
 /* 1 – Construa um algoritmo em PHP que leia 20 valores inteiros e calcule seu somatório. */


'''

soma = 0
for i in range(20):
    soma = soma + i
    print(soma)

'''
 /* 2 – Construa um algoritmo que solicite ao usuário um valor entre 10 e 100, caso o usuário digite 
    um valor menor que 10 ou maior que 100, envie uma mensagem informando que os valores são inválidos 
    caso contrário conte de zero até o numero digitado pelo usuário. */
'''

valor = input("Insira o valor: ")
numero = int(valor)

if numero <= 10 or numero >= 100:
    print("Valor Invalido")
else:
    for i in range(numero+1):
        print(i)

'''
/* 3 - Escreva um programa que calcule e mostre a tabuada de multiplicação (até 10x) de um número qualquer 
    informado através de uma variável. */
    
'''
tabuada = 5
for i in range(11):
    print("{} x {} =".format(tabuada,i), tabuada * i)


'''
/* 4 - Criar um algoritmo em Python para ler 2 números  e mostrar todos os números pares entre eles (inclusive) *

'''
num1 = 1
num2 = 10

if num2 < num1:
    temp = num1
    num1 = num2
    num2 = temp

while num1 <= num2:
        if (num1 % 2) == 0:
            print(num1)
        num1 = num1 + 1