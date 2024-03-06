from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

# Configurações do servidor
HOST = "localhost"
PORT = 8000

# Variável para armazenar a diferença de tempo
time_difference = 0

# Classe do servidor
class BerkeleyServer:
    def get_time(self):
        return datetime.now().timestamp()

    def calculate_time_difference(self, client_time):
        server_time = datetime.now().timestamp()
        global time_difference
        time_difference = server_time - client_time
        return time_difference

    def adjust_time(self):
        current_time = datetime.now().timestamp()
        adjusted_time = current_time + time_difference
        return adjusted_time

# Configuração do servidor RPC
server = SimpleXMLRPCServer((HOST, PORT), requestHandler=SimpleXMLRPCRequestHandler, allow_none=True)
server.register_instance(BerkeleyServer())

print(f"Servidor Berkeley RPC rodando em {HOST}:{PORT}")
server.serve_forever()
