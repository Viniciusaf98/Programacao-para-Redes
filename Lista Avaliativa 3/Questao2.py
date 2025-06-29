import socket, sys
from urllib.parse import urlparse

# ----------------------------------------------------------------------
PORT = 80
CODE_PAGE = 'utf-8'
BUFFER_SIZE = 2048
# ----------------------------------------------------------------------

url = input('\nInforme a URL completa (ex: http://example.com): ')

parsed_url = urlparse(url)
host = parsed_url.hostname
path = parsed_url.path if parsed_url.path else '/'

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.settimeout(5)

try:
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    # Montar a requisição HTTP GET
    requisicao = f'GET {path} HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\nConnection: close\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        resposta_completa = b''
        while True:
            dados = tcp_socket.recv(BUFFER_SIZE)
            if not dados:
                break
            resposta_completa += dados

        # Decodificar e separar o HEADER do corpo da resposta
        resposta_str = resposta_completa.decode(CODE_PAGE, errors='ignore')
        header, _, corpo = resposta_str.partition('\r\n\r\n')

        # Verificar se o Content-Length está presente no header
        content_length = None
        for linha in header.split('\r\n'):
            if linha.lower().startswith('content-length:'):
                content_length = int(linha.split(':')[1].strip())
                break

        # Caso Content-Length esteja presente, controlar o tamanho
        if content_length:
            while len(corpo.encode(CODE_PAGE)) < content_length:
                dados = tcp_socket.recv(BUFFER_SIZE)
                if not dados:
                    break
                corpo += dados.decode(CODE_PAGE, errors='ignore')

        # Salvar o corpo da resposta em output.html
        with open('output.html', 'w', encoding=CODE_PAGE) as arquivo:
            arquivo.write(corpo)
        print('\nConteúdo salvo em output.html')

    tcp_socket.close()
