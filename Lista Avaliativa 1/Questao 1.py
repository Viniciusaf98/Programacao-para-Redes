import sys
import json
import os
from questao_lib import ip2bin, cidr2mascara, bit2bitAND, bin2ip, gerar_nome_arquivo 
from tabulate import tabulate

def calcular_subredes(ip, mascara_inicial, mascara_final):
    resultados = {}
    for cidr in range(mascara_inicial, mascara_final + 1):
        try:
            ip_bin = ip2bin(ip)
            mascara_decimal, mascara_bin = cidr2mascara(cidr)
            rede_bin = bit2bitAND(ip_bin[1], mascara_bin)
            rede_dec = bin2ip(rede_bin)
            
            # Calcula o Broadcast.
            broadcast_bin = rede_bin[:cidr] + '1' * (32 - cidr)
            broadcast_dec = bin2ip(broadcast_bin)

            # Calcula o Primeiro Host.
            primeiro_host_bin = rede_bin[:31] + '1'
            primeiro_host_dec = bin2ip(primeiro_host_bin)

            # Calcula o Último Host.
            ultimo_host_bin = broadcast_bin[:-1] + '0'
            ultimo_host_dec = bin2ip(ultimo_host_bin)
            
            hosts_validos = (2 ** (32 - cidr)) - 2
            
            resultados[f"/{cidr}"] = {
                "Rede": rede_dec,
                "Primeiro Host": primeiro_host_dec,
                "Último Host": ultimo_host_dec,
                "Broadcast": broadcast_dec,
                "Máscara Decimal": mascara_decimal,
                "Máscara Binária": mascara_bin,
                "Hosts Válidos": hosts_validos
            }
        except Exception as e:
            print(f"Erro ao processar CIDR /{cidr}: {e}")
    
    return resultados

# Solicita entradas do usuário e calcula as sub-redes.

if __name__ == "__main__":
    strIPaddress = input("Informe o endereço IP: ")
    intMascaraInicial = int(input("Informe a máscara inicial: "))
    intMascaraFinal = int(input("Informe a máscara final: "))

    resultados = calcular_subredes(strIPaddress, intMascaraInicial, intMascaraFinal)
    
    # Exibe os resultados em uma tabela

    dados_tabulate = [
        [cidr, detalhes["Rede"], detalhes["Primeiro Host"], detalhes["Último Host"],
         detalhes["Broadcast"], detalhes["Máscara Decimal"], detalhes["Máscara Binária"], detalhes["Hosts Válidos"]]
        for cidr, detalhes in resultados.items()
    ]
    cabecalhos = ["Máscara", "Rede", "Primeiro Host", "Último Host", "Broadcast", "Máscara Decimal", "Máscara Binária", "Hosts Válidos"]
    print(tabulate(dados_tabulate, headers=cabecalhos, tablefmt="grid"))   

nome_arquivo = gerar_nome_arquivo("subredes_resultados", "json")

# Salvar os resultados no arquivo JSON

with open(nome_arquivo, 'w', encoding='utf-8') as f:
    json.dump(resultados, f, indent=4, ensure_ascii=False)
print(f"\nResultados salvos em {nome_arquivo}")