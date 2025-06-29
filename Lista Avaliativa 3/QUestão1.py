import socket
import sys

# ----------------------------------------------------------------------
# Constantes do Programa
PORT        = 80
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 2048
# ----------------------------------------------------------------------

# Solicitar a URL do usuário
host = input('\nInforme o nome do HOST ou URL do site (sem http/https): ')

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.settimeout(5)

try:
    # Conectar ao host na porta 80
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    requisicao = f'HEAD / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    try:
        # Enviar a requisição HEAD
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        # Receber a resposta e processar os cabeçalhos
        resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
        print('-'*50)
        print(resposta)
        print('-'*50)

        # Separar os cabeçalhos e gerar o dicionário
        linhas = resposta.split('\r\n')
        cabecalhos = {}
        for linha in linhas[1:]:  # Ignorar a primeira linha (status line)
            if ': ' in linha:
                chave, valor = linha.split(': ', 1)
                cabecalhos[chave] = valor

        # Exibir o dicionário na tela
        print('\nDicionário dos cabeçalhos HTTP:')
        for chave, valor in cabecalhos.items():
            print(f'{chave}: {valor}')
    tcp_socket.close()
