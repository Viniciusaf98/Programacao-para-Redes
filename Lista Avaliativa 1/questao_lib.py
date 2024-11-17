import os

# Função para converter um endereço IP em formato decimal para binário.

def ip2bin(ip):
    try:
        octetos = list(map(int, ip.split('.')))
        if len(octetos) != 4 or not all(0 <= o <= 255 for o in octetos):
            raise ValueError("IP inválido.")
        ip_bin = ''.join(f'{octeto:08b}' for octeto in octetos)
        return (ip, ip_bin)
    except Exception as e:
        raise ValueError(f"Erro na conversão do IP: {e}")

# Função para converter uma máscara no formato CIDR para os formatos decimal e binário.

def cidr2mascara(cidr):
    if not (0 <= cidr <= 32):
        raise ValueError("Máscara CIDR inválida.")
    mascara_bin = '1' * cidr + '0' * (32 - cidr)
    octetos = [int(mascara_bin[i:i + 8], 2) for i in range(0, 32, 8)]
    mascara_decimal = '.'.join(map(str, octetos))
    return (mascara_decimal, mascara_bin)

# Função para calcular o endereço de rede realizando a operação AND bit a bit.

def bit2bitAND(ip_bin, mascara_bin):
    if len(ip_bin) != len(mascara_bin):
        raise ValueError("IP e máscara não têm o mesmo comprimento.")
    rede_bin = ''.join(str(int(a) & int(b)) for a, b in zip(ip_bin, mascara_bin))
    return rede_bin

# Função para converter uma string binária de 32 bits em um endereço IP decimal.

def bin2ip(bin_str):
    if len(bin_str) != 32:
        raise ValueError("Binário inválido.")
    octetos = [int(bin_str[i:i + 8], 2) for i in range(0, 32, 8)]
    return '.'.join(map(str, octetos))

# Função para criar um nome de arquivo único, verificar se o arquivo existe e adiciona um contador ao nome, caso exista algum com o mesmo nome.

def gerar_nome_arquivo(base_nome, extensao):
    """
    Gera um nome de arquivo único para evitar sobrescrita.
    Verifica se o arquivo já existe no diretório atual e incrementa um contador no nome.
    """
    contador = 1
    nome_arquivo = f"{base_nome}.{extensao}"
    while os.path.exists(nome_arquivo):
        nome_arquivo = f"{base_nome}_{contador}.{extensao}"
        contador += 1
    return nome_arquivo