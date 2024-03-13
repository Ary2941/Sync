from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

import logging

logging.basicConfig(level=logging.WARNING)



# Configurações do servidor
HOST = "localhost"
PORT = 8000

# Classe do servidor
class BerkeleyServer:
    def __init__(self):
        self.client_times = []

    def get_time(self):
        return datetime.now().timestamp()

    def add_client_time(self, client_time):
        self.client_times.append(client_time)
        print(f"Tempo do cliente adicionado: {client_time}")
        return True

    def calculate_average_time(self):
        server_time = datetime.now().timestamp()
        all_times = [server_time] + self.client_times
        average_time = sum(all_times) / len(all_times)
        return average_time

    def request_client_time(self):
        return True

# Configuração do servidor RPC
server = SimpleXMLRPCServer((HOST, PORT), requestHandler=SimpleXMLRPCRequestHandler, allow_none=True)
server.register_instance(BerkeleyServer())

print(f"Servidor Berkeley RPC rodando em {HOST}:{PORT}")

# Aguarda a conexão do cliente e solicita seu tempo
while True:
    server.handle_request()