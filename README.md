# Pratica Spark 06

## Descrição 

O projeot implementa uma pipeline de dados em tempo real, das apis da CoinGecko e Smart Citizen. O ambiente é conteinerizado com Docker, executando o Apache Spark em modo streaming para processar dados os coletados. Também demonstra o uso de data lakes (MinIO/S3) para escalabilidade e persistência.

---

## Arquitetura

A solução é composta por múltiplos serviços orquestrados via Docker Compose:

* Spark (master + workers)
* Serviço Python para coleta de dados
* MinIO como data lake

O script `coleta.py` consulta as APIs, salvando as respostas em JSON no diretório `/data_input`. Isso simula a ingestão de dados IoT expostos via HTTP.

O script `spark_streaming.py` lê esses arquivos no Spark Structured Streaming, permitindo transformações como filtros, agregações e análise de anomalias. Os resultados podem ser salvos no data lake em formato Parquet, viabilizando posterior análise ou machine learning.

Streaming garante reação imediata a eventos e decisões em tempo quase real, ao contrário do batch. Além disso, conteinerizar o ambiente facilita a replicação do experimento e reduz problemas de infraestrutura.
---

## Estrutura

```plaintext
├── docker-compose.yml
├── app/
│   ├── coleta.py
│   ├── spark_streaming.py
│   ├── requirements.txt
│   └── Dockerfile
└── data_input/
```

---

## Sobre a API CoinGecko

Nesta prática foi utilizada a **CoinGecko API** ([documentação](https://www.coingecko.com/en/api/documentation)) para simular a coleta de dados financeiros em tempo real.

* **Dados coletados**: preços atualizados de criptomoedas (Bitcoin, Ethereum) em diversas moedas fiduciárias.
* **Frequência**: resposta imediata (atrasa apenas do tempo de latencia da prorpia rede), valores de mercado praticamente em tempo real.
* **Granularidade**: dados pontuais de preço.

O script `coleta.py` faz chamadas periódicas a este endpoint e salva as cotações em JSON, para o processamento no Spark Streaming.

---

## Execução

1. **Subir os containers**

   ```bash
   docker compose up --build -d
   ```

2. **Verificar serviços**

   ```bash
   docker compose ps
   ```

3. **Rodar o job do Spark**

   ```bash
   docker exec -it spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client /app/spark_streaming.py
   ```

4. **Monitorar Spark UI**
   [http://localhost:8080](http://localhost:8080)

5. **(Opcional) Acessar MinIO**
   [http://localhost:9001](http://localhost:9001)

---
### Diretórios
![Diretorios](https://github.com/user-attachments/assets/81de0243-68e6-4fe6-92a2-02b708deb13c)

### Containers em execução
![Containers rodando](https://github.com/user-attachments/assets/eb264fb5-0868-4520-b49d-7f317882c7e9)

### Interface Spark local
![Spark local](https://github.com/user-attachments/assets/3b92638d-4682-47a1-8203-5e76c488f8a6)
