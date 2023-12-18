""" Vamos criar um jogo da forca simples em Python usando funções. Neste jogo, o computador escolherá uma palavra aleatória e o jogador tentará adivinhar as letras. Vamos criar funções para inicializar o jogo, mostrar a palavra oculta, receber palpites e verificar se o jogo foi ganho ou perdido. """

import random

def escolher_palavra():
    """Escolhe aleatoriamente uma palavra da lista."""
    palavras = ["python", "programacao", "computador", "teclado", "desenvolvimento"]
    return random.choice(palavras) #choice() retorna um elemento aleatorio de uma lista especifica

def exibir_palavra_oculta(palavra, letras_certas):
    """Exibe a palavra oculta com as letras corretas adivinhadas."""
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_certas:
            palavra_oculta += letra
        else:
            palavra_oculta += " _ "
    return palavra_oculta

def jogar_forca():
    """Função principal para o jogo da forca."""
    palavra_secreta = escolher_palavra()
    print(type(palavra_secreta))
    
    
    letras_corretas = []
    print(type(letras_corretas))
    tentativas = 6  # Número máximo de tentativas

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        palavra_atual = exibir_palavra_oculta(palavra_secreta, letras_corretas)
        print("\nPalavra Atual:", palavra_atual)
        
        # Solicitar uma letra ao jogador
        letra = input("Digite uma letra: ").lower() #Converte para letras minusculas

        #Testa se digitou uma letra correta anterioemente 
        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente novamente!")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra) #append adiciona dados em um item
            print("Letra correta! :)")
        else:
            tentativas -= 1
            print("Letra incorreta. Você tem", tentativas, "tentativas restantes.")

        # Verificar se o jogador ganhou
        if set(letras_corretas) == set(palavra_secreta):
            print(type(palavra_secreta))
            print(type(letras_corretas))
            print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    # Verificar se o jogador perdeu
    if tentativas == 0:
        print("\nVocê perdeu! A palavra correta era:", palavra_secreta)

# Iniciar o jogo
jogar_forca()
