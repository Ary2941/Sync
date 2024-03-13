# Berkeley Clock Synchronization using RPC

Este é um projeto simples que implementa o algoritmo de Berkeley para sincronização de relógios em uma rede local usando RPC (Remote Procedure Call). O servidor recebe o tempo de cada cliente, calcula a diferença de tempo e envia a diferença de volta aos clientes para ajustar seus relógios.

## Configuração do Ambiente

Certifique-se de ter o Python instalado na sua máquina antes de executar o projeto.

### Dependências

O projeto utiliza as seguintes bibliotecas Python:

- `xmlrpc.server`
- `xmlrpc.client`
- `datetime`
- `time`
- `asyncio` (para versão assíncrona do cliente)

### Execução
```bash
client.py
```
em outro teminal os servidores

``` bash
server.py
```
