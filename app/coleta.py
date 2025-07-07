import requests
import json
import time
import os

os.makedirs("/data_input", exist_ok=True)

def coletar_dado():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    r = requests.get(url)
    data = r.json()
    leitura = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "bitcoin_usd": data["bitcoin"]["usd"],
        "ethereum_usd": data["ethereum"]["usd"]
    }
    nome_arquivo = f"/data_input/leitura_{int(time.time())}.json"
    with open(nome_arquivo, 'w') as f:
        json.dump(leitura, f)
    print(f"Salvo: {nome_arquivo} | {leitura}")

if __name__ == "__main__":
    while True:
        try:
            coletar_dado()
            time.sleep(5)
        except Exception as e:
            print(f"Erro: {e}")
