from tabulate import tabulate
from funcoes import encontrar_nonce

def gerar_resultados():
    # Lista de testes com os textos e os bits desejados
    testes = [
        ("Texto simples", 8),
        ("Texto simples", 10),
        ("Texto simples", 15),
        ("Texto maior altera tempo?", 8),
        ("Texto maior altera tempo?", 10),
        ("Texto maior altera tempo?", 15),
        ("Pode calcular isso?", 18),
        ("Pode calcular isso?", 19),
        ("Pode calcular isso?", 20)
    ]
    
    resultados = []
    
    for texto, bits in testes:
        # Converte o texto para bytes
        dados_bytes = texto.encode('utf-8')
        # Chama a função para encontrar o nonce e o tempo gasto
        nonce_encontrado, tempo_gasto = encontrar_nonce(dados_bytes, bits)
        # Armazena os resultados na lista
        resultados.append([texto, bits, nonce_encontrado, f"{tempo_gasto:.6f}"])
    
    # Exibe a tabela no terminal com a formatação
    print(tabulate(resultados, headers=["Texto para Validar", "Bits Zero", "Nonce", "Tempo (s)"], tablefmt="fancy_grid"))
    
    # Salva a tabela no arquivo 'resultados.txt'
    with open("resultados.txt", "w") as arquivo:
        arquivo.write(tabulate(resultados, headers=["Texto para Validar", "Bits Zero", "Nonce", "Tempo (s)"], tablefmt="fancy_grid"))
    
    print("Tabela salva no arquivo: 'resultados.txt'.")

if __name__ == "__main__":
    gerar_resultados()
