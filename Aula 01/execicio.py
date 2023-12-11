'''
 1 - Elabore um algoritmo para ler um valor inteiro e informar,
        através de uma mensagem se este valor é um número par ou ímpar.
'''
valor = input("Informe um valor: ")
print(type(valor))

numero = int(valor)
print(type(numero))

resto = numero%2
print(resto)

if resto == 0:
    print("Número par")
else:
    print("Numero impar")

'''
* 2 - Implemente um programa que leia dois valores inteiros e verificar se o primeiro 
     * é múltiplo do segundo, 
     * seu programa deverá exibir a mensagem: “São múltiplos” ou “Não são múltiplos” 
'''

valor_um = 30
valor_dois = 30

restom = valor_um%valor_dois
print(restom)

if valor_um%valor_dois==0:
    print("Multiplos")
else:
    print("Não multiplos")

'''
 * 3 - Desenvolva um programa para ler um valor inteiro e apresentar
     *  a. Exibir a mensagem “número negativo” se n < 0.
     *  b. Exibir a mensagem “zero” se n = 0.
     *  c. Exibir a mensagem “número positivo” se n > 0.
     
'''
valor_inteiro = -10

if valor_inteiro < 0:
    #print("o valor {} é negativo".format(valor_inteiro))
    print("o valor é negativo")
elif valor_inteiro == 0:
    print("o valor {} é zero".format(valor_inteiro))
elif valor_inteiro > 0:
    print("o valor {} é positivo".format(valor_inteiro))
else:
    print("o valor {} é desconhecido".format(valor_inteiro))


'''
 * 4 - Escreva um programa para que leia um número e verifique 
     * se ele se encontra no intervalo entre 5 e 20.
     */

     /**
      *Comparadores lógicos 
      * && - A duas condições ou mais devem ser verdadeiras (conectivo e)
      * || - Umas das alternativas deve ser veradeiras ( conectivo ou )      * 

'''
num = 6
if num >= 5 and num <= 20:
    print("O numero esta no intervalo entre 5 e 20")
else:
    print("O numero não esta no intervalo entre 5 e 20")

'''
 * 5 - Desenvolva um programa para ler dois valores inteiros e apresentar 
     * a adição destes valores quando o x > y, caso contrário, 
     * deve ser efetuado a multiplicação deles.
'''

x = 2
y = 5

if x > y:
    print("a soma dos valores é: ", x + y)
else:
    print("a multiplicação dos valores é: ", x * y)
