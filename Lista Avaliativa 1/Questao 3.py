import random

# Vai carregar o arquivo txt e verificar se as palavras possuem entre 5 e 8 letras.

def carregar_palavra(arquivo="questao3.txt"):
    return [linha.strip().upper() for linha in open(arquivo, "r") if 5 <= len(linha.strip()) <= 8]

# Vai sortear uma palavra aleatória da lista de palavras.

def sortear_palavra(lista_palavra):
    return random.choice(lista_palavra)

# Vai comparar a palavra digitada pelo usuário com a palavra sorteada, fornecendo feedback sobre a tentativa.

def verificar_palavra(tentativa, palavra_sorteada):
    palavra_sorteada_processada = [False] * len(palavra_sorteada)
    tentativa_processada = [False] * len(tentativa)
    
    # Inicia o resultado da comparação
    resultado = ["" for _ in tentativa]
    
    # Primeira etapa: letras na posição correta (verde)
    for i in range(len(tentativa)):
        if tentativa[i] == palavra_sorteada[i]:
            resultado[i] = f"\033[32m{tentativa[i]}\033[0m"  # Verde
            palavra_sorteada_processada[i] = True
            tentativa_processada[i] = True

    # Segunda etapa: letras corretas na palavra, mas em posição incorreta (amarelo)
    for i in range(len(tentativa)):
        if not tentativa_processada[i]:
            for j in range(len(palavra_sorteada)):
                if (
                    tentativa[i] == palavra_sorteada[j]
                    and not palavra_sorteada_processada[j]
                ):
                    resultado[i] = f"\033[33m{tentativa[i]}\033[0m"  # Amarelo
                    palavra_sorteada_processada[j] = True
                    tentativa_processada[i] = True
                    break

    # Terceira etapa: letras que não estão na palavra (vermelho)
    for i in range(len(tentativa)):
        if not resultado[i]:
            resultado[i] = f"\033[31m{tentativa[i]}\033[0m"  # Vermelho

    return " ".join(resultado)

# Inicia o jogo, configurando as tentativas e exibindo a mensagem inicial para o usuário.
def jogar():
    palavras = carregar_palavra("questao3.txt")
    palavra_sorteada = sortear_palavra(palavras)
    tentativas_restantes = 6
    tamanho_palavra = len(palavra_sorteada)
    
    print(f"\033[36mBem-vindo à minha imitação do Termo!\033[0m")
    print(f"A palavra sorteada é o nome de um jogo e tem \033[35m{tamanho_palavra} letras\033[0m. Você tem 6 tentativas. Boa sorte!")
    
    while tentativas_restantes > 0:
        tentativa = input(f"Tentativa ({tentativas_restantes} restantes): ").strip().upper()
        
        if len(tentativa) != tamanho_palavra:
            print(f"\033[31mA palavra deve ter {tamanho_palavra} letras!\033[0m")
            continue
        
        feedback = verificar_palavra(tentativa, palavra_sorteada)
        print("Feedback:", feedback)
        
        if tentativa == palavra_sorteada:
            print(f"\033[32mParabéns! Você acertou a palavra '{palavra_sorteada}' em {6 - tentativas_restantes + 1} tentativas!\033[0m")
            return
        
        tentativas_restantes -= 1
    
    print(f"\033[31mVocê perdeu! A palavra era '{palavra_sorteada}'.\033[0m")

if __name__ == "__main__":
    jogar()
