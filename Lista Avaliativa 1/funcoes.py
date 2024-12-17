import hashlib
import time

def calcular_hash(dados):
    """Calcula o hash SHA-256 dos dados fornecidos"""
    return hashlib.sha256(dados).hexdigest()

def encontrar_nonce(dados_para_hash, bits_iniciais_zero):
    """Encontra o nonce que faz com que o hash tenha os bits iniciais zero especificados"""
    nonce = 0
    tempo_inicial = time.time()
    
    # Define o valor alvo baseado na quantidade de bits zero desejados
    alvo = (1 << (256 - bits_iniciais_zero))

    while True:
        # Adiciona o nonce aos dados e calcula o hash
        dados_com_nonce = dados_para_hash + nonce.to_bytes((nonce.bit_length() + 7) // 8, 'big')
        resultado_hash = calcular_hash(dados_com_nonce)
        
        # Converte o hash de hexadecimal para binário
        hash_binario = bin(int(resultado_hash, 16))[2:].zfill(256)
        
        # Verifica se os primeiros bits do hash são zero conforme solicitado
        if hash_binario[:bits_iniciais_zero] == '0' * bits_iniciais_zero:
            break
        
        nonce += 1
    
    tempo_final = time.time() - tempo_inicial
    return nonce, tempo_final
