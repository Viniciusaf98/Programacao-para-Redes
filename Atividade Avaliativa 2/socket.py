import socket
import json

# Função para testar a porta
def testar_porta(host, porta, protocolo):
    try:
        if protocolo == 'TCP':
            # Tentar conectar usando TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Timeout de 1 segundo
                s.connect((host, porta))
        elif protocolo == 'UDP':
            # Tentar conectar usando UDP
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)  # Timeout de 1 segundo
                s.sendto(b'Ping', (host, porta))
        return 'OK'
    except Exception as e:
        return str(e)

# Função para carregar os dados do arquivo JSON
def carregar_dados_json():
    with open('dados.json', 'r') as f:
        return json.load(f)

# Função para testar as portas
def testar_portas(host):
    dados = carregar_dados_json()
    resultados = []

    for i, porta_info in enumerate(dados):
        porta = porta_info['porta']
        protocolo = porta_info['protocolo']
        descricao = porta_info['descricao']
        status = testar_porta(host, porta, protocolo)
        resultados.append({
            i + 1: {
                'porta': porta,
                'protocolo': f'{protocolo} – {descricao}',
                'status': status
            }
        })

    # Salvar os resultados em formato JSON
    with open("teste_porta.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

# Função principal que solicita o host e realiza os testes
if __name__ == '__main__':
    host = input("Informe o host (IP ou nome de domínio) para testar as portas: ")
    testar_portas(host)
    print("Teste concluído. Os resultados foram salvos em 'teste_porta.json'.")
