from xmlrpc.client import ServerProxy
from datetime import datetime
import asyncio


# Configurações do cliente
SERVER_ADDRESS = "http://localhost:8000"
UPDATE_INTERVAL = 5  # Intervalo de atualização em segundos

async def update_time(server):
    while True:
        # Obtém o tempo do cliente
        client_time = datetime.now().timestamp()
        print("enviando tempo para o server...")
        server.request_client_time()
        time_difference = server.add_client_time(client_time)
        adjusted_time = server.calculate_average_time()

        print(f"Tempo do cliente: {client_time}")
        print(f"Diferença de tempo recebida do servidor: {time_difference}")
        print(f"Tempo ajustado no cliente: {adjusted_time}")
        print("----")

        # Aguarda o intervalo antes da próxima atualização
        await asyncio.sleep(UPDATE_INTERVAL)

# Conecta ao servidor RPC
server = ServerProxy(SERVER_ADDRESS, allow_none=True)

# Inicia o loop de atualização assíncrono
asyncio.run(update_time(server))
