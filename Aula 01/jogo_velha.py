def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro atual."""
    for linha in tabuleiro:
        print(" ".join(linha))

def verificar_vencedor(tabuleiro):
    """Verifica se há um vencedor."""
    # Verificar linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False

def jogar_jogo_da_velha():
    """Função principal para o jogo da velha."""
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]  # Inicializar o tabuleiro
    jogador_atual = "X"  # Começar com o jogador X

    print("Bem-vindo ao Jogo da Velha!")

    for _ in range(9):  # Número máximo de movimentos é 9
        exibir_tabuleiro(tabuleiro)

        # Solicitar movimento ao jogador
        linha = int(input(f"Jogador {jogador_atual}, digite o número da linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, digite o número da coluna (0, 1, 2): "))

        # Verificar se a posição está vazia
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Posição ocupada. Tente novamente.")
            continue

        # Verificar se há um vencedor
        if verificar_vencedor(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print(f"\nParabéns! Jogador {jogador_atual} venceu!")
            break

        # Alternar para o próximo jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        exibir_tabuleiro(tabuleiro)
        print("\nEmpate! O jogo terminou sem vencedor.")

# Iniciar o jogo
jogar_jogo_da_velha()
