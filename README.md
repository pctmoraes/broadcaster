# Broadcaster

Chat em tempo real com Websocket.
<br>

## Instruções para execução do projeto
## Pre-requisitos:
- repositório clonado <br>
- python e pip instalados
<br>

1. Acesse a pasta -> `cd broadcaster`
2. Execute o comando para instalação das dependências -> `pip install -r requirements.txt`
3. Execute o comando para rodar o servidor -> `uvicorn main:app --reload`
    - Por padrão o servidor irá utilizar a porta 8000, mas é possível alterar passando uma outra porta através da flag --port, por exemplo -> `uvicorn main:app --port 8080 --reload`

### Tecnologias utilizadas
- Python 3.10
- FastAPI
- Uvicorn
- WebSocket