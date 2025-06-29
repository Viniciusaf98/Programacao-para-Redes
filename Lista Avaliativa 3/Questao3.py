import socket
import sys
import os

# ----------------------------------------------------------------------
PORT = 80
BUFFER_SIZE = 2048
# ----------------------------------------------------------------------

def download_file(url):
    # Removendo o esquema (http:// ou https://) se presente
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]

    # Separando o host e o caminho
    if '/' in url:
        host, path = url.split('/', 1)
        path = '/' + path
    else:
        host = url
        path = '/'

    file_name = os.path.basename(path)
    
    # Cria o socket TCP
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(5)

    try:
        tcp_socket.connect((host, PORT))
    except Exception as e:
        print(f'\nERRO ao conectar.... {e}')
        return

    # Enviando a requisição GET
    requisicao = f'GET {path} HTTP/1.1\r\nHOST: {host}\r\nConnection: close\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode('utf-8'))
    except Exception as e:
        print(f'\nERRO ao enviar requisição.... {e}')
        tcp_socket.close()
        return

    # Recebendo a resposta
    resposta = b''
    while True:
        dados = tcp_socket.recv(BUFFER_SIZE)
        if not dados:
            break
        resposta += dados

    tcp_socket.close()

    # Separando o cabeçalho do conteúdo
    header_end = resposta.find(b'\r\n\r\n')
    headers = resposta[:header_end].decode('utf-8')
    conteudo = resposta[header_end+4:]

    # Verificando o tamanho do conteúdo
    content_length = None
    for linha in headers.split('\r\n'):
        if linha.lower().startswith('content-length:'):
            content_length = int(linha.split(':')[1].strip())
            break

    # Se Content-Length estiver presente, garantir que todo o conteúdo foi baixado
    if content_length:
        while len(conteudo) < content_length:
            dados = tcp_socket.recv(BUFFER_SIZE)
            if not dados:
                break
            conteudo += dados

    # Salvando o arquivo
    try:
        with open(file_name, 'wb') as f:
            f.write(conteudo)
        print(f'Arquivo "{file_name}" salvo com sucesso!')
    except Exception as e:
        print(f'Erro ao salvar o arquivo: {e}')

if __name__ == "__main__":
    url = input("Informe a URL completa da imagem ou arquivo: ")
    download_file(url)
