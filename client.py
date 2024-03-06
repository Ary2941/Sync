from xmlrpc.client import ServerProxy
from datetime import datetime
import asyncio

# Configurações do cliente
SERVER_ADDRESS = "http://localhost:8000"
UPDATE_INTERVAL = 5  # Intervalo de atualização em segundos

async def update_time():
    while True:
        # Obtém o tempo do cliente
        client_time = datetime.now().timestamp()

        # Envia o tempo ao servidor e recebe a diferença de tempo
        server.calculate_time_difference(client_time)

        # Ajusta o tempo no cliente com base na diferença de tempo recebida do servidor
        adjusted_time = server.adjust_time()

        print(f"Tempo do cliente: {client_time}")
        print(f"Tempo ajustado no cliente: {adjusted_time}")
        print("----")

        # Aguarda o intervalo antes da próxima atualização
        await asyncio.sleep(UPDATE_INTERVAL)

# Conecta ao servidor RPC
server = ServerProxy(SERVER_ADDRESS, allow_none=True)

# Inicia o loop de atualização assíncrono
asyncio.run(update_time())
