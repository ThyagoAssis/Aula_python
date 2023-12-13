import random
print("--------------------------------")
print("Bem vindo ao Jogo da adivinhação")
print("--------------------------------")

numero_secreto = random.randrange(1,101)
#print(numero_secreto)
tentativas = 0
rodada = 1
pontos = 1000

nivel = int(input("Escolha seu nível: (1) Fácil, (2) Médio, (3) Difícil: "))

if nivel == 1:
    tentativas = 20
    print(f"Você escolheu o nível {nivel} e terá {tentativas} rodadas. ")

elif nivel == 2:
    tentativas = 10
    print(f"Você escolheu o nível {nivel} e terá {tentativas} rodadas. ")

elif nivel == 3:
    tentativas = 5
    print(f"Você escolheu o nível {nivel} e terá {tentativas} rodadas. ")

else:
    print("Opção invalida!")

#Rodadas
while rodada <= tentativas:
    print("Tentativa {} de {}".format(rodada,tentativas))
    chute = int(input("Informe um valor entre 1 e 100: "))

    #Verifica entre 1 e 100
    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        rodada += 1
        continue

    #Testa os chutes
    if chute == numero_secreto:
        print("Você acertou!")
        break
    elif numero_secreto > chute:
        print("Você errou. Seu chute foi menor")
    elif numero_secreto < chute:
        print("Você errou. Seu chute foi maior")
    rodada += 1

print("Fim do jogo")

