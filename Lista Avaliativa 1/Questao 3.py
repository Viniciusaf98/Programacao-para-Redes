import random
from colorama import Fore, Style, init

init(autoreset=True)

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
    
    # Inicia o resultado da comparação, marcando as letras corretas (posição e letra) como verdes
    resultado = [Fore.GREEN + tentativa[i] + Style.RESET_ALL if tentativa[i] == palavra_sorteada[i] else ""
                 for i in range(len(tentativa))]
    
     # Atualiza os marcadores para as letras que foram acertadas na posição correta
    for i in range(len(tentativa)):
        if resultado[i]:
            palavra_sorteada_processada[i] = True
            tentativa_processada[i] = True
    
    # Agora, verifica as letras que estão na palavra, mas não na posição correta
    resultado = [
        Fore.YELLOW + tentativa[i] + Style.RESET_ALL if (not tentativa_processada[i] and
                                                         any(tentativa[i] == palavra_sorteada[j] and
                                                             not palavra_sorteada_processada[j] for j in range(len(palavra_sorteada))))
        else resultado[i]  
        for i in range(len(tentativa))
    ]
    
    # Atualiza os marcadores para as letras que foram identificadas como amarelas
    for i in range(len(tentativa)):
        if resultado[i] == Fore.YELLOW + tentativa[i] + Style.RESET_ALL:
            for j in range(len(palavra_sorteada)):
                if tentativa[i] == palavra_sorteada[j] and not palavra_sorteada_processada[j]:
                    palavra_sorteada_processada[j] = True
                    tentativa_processada[i] = True
                    break
    
    # Marca as letras que não estão na palavra como vermelhas
    resultado = [
        Fore.RED + tentativa[i] + Style.RESET_ALL if resultado[i] == "" else resultado[i]
        for i in range(len(tentativa))
    ]
    
    return " ".join(resultado)
    
# Inicia o jogo, configurando as tentativas e exibindo a mensagem inicial para o usuário.
def jogar():
    palavras = carregar_palavra("questao3.txt")
    palavra_sorteada = sortear_palavra(palavras)
    tentativas_restantes = 6
    tamanho_palavra = len(palavra_sorteada)
    
    print(f"{Fore.CYAN}Bem-vindo à minha imitação do Termo!{Style.RESET_ALL}")
    print(f"A palavra sorteada é o nome de um jogo e tem {Fore.MAGENTA}{tamanho_palavra} letras{Style.RESET_ALL}. Você tem 6 tentativas. Boa sorte!")
    
    while tentativas_restantes > 0:
        tentativa = input(f"Tentativa ({tentativas_restantes} restantes): ").strip().upper()
        
        if len(tentativa) != tamanho_palavra:
            print(f"{Fore.RED}A palavra deve ter {tamanho_palavra} letras!{Style.RESET_ALL}")
            continue
        
        feedback = verificar_palavra(tentativa, palavra_sorteada)
        print("Feedback:", feedback)
        
        if tentativa == palavra_sorteada:
            print(f"{Fore.GREEN}Parabéns! Você acertou a palavra '{palavra_sorteada}' em {6 - tentativas_restantes + 1} tentativas!{Style.RESET_ALL}")
            return
        
        tentativas_restantes -= 1
    
    print(f"{Fore.RED}Você perdeu! A palavra era '{palavra_sorteada}'.{Style.RESET_ALL}")

if __name__ == "__main__":
    jogar()
