import os

# Função para criptografar o conteúdo aplicando XOR com a palavra-passe
def aplicar_criptografia(dados, chave):
    chave_comprimento = len(chave)
    # Usando list comprehension para aplicar a operação XOR
    dados_criptografados = [
        byte ^ ord(chave[i % chave_comprimento])  # XOR entre o byte do arquivo e o valor ASCII do caractere da chave
        for i, byte in enumerate(dados)  # Enumerate para pegar o índice e o byte do arquivo
    ]
    return bytes(dados_criptografados)  # Converte a lista de volta para bytes

# Função para gerenciar a leitura e escrita dos arquivos
def processar_arquivos():
    arquivo_origem = input("Informe o arquivo de origem: ")
    palavra_chave = input("Informe a palavra-chave: ")
    arquivo_destino = input("Informe o arquivo de destino: ")

    # Verifica se o arquivo de origem existe
    if not os.path.exists(arquivo_origem):
        print("ERRO: O arquivo de origem não foi encontrado.")
        return

    # Verifica se o arquivo de destino já existe
    if os.path.exists(arquivo_destino):
        print("ERRO: O arquivo de destino já existe. Não será sobrescrito.")
        return

    try:
        # Abre o arquivo de origem para leitura no modo binário
        with open(arquivo_origem, 'rb') as origem:
            conteudo_origem = origem.read()

        # Aplica a criptografia ao conteúdo lido, usando a palavra-chave
        conteudo_criptografado = aplicar_criptografia(conteudo_origem, palavra_chave)

        # Abre o arquivo de destino para escrita no modo binário
        with open(arquivo_destino, 'wb') as destino:
            destino.write(conteudo_criptografado)

        print(f"Arquivo processado e salvo como: '{arquivo_destino}'.")

    except Exception as erro:
        print(f"ERRO: {erro}")  # Exibe a mensagem de erro, caso ocorra algum problema

# Execução do programa principal
if __name__ == "__main__":
    processar_arquivos()
