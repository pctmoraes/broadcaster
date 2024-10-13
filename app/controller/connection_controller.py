from random import randint
from fastapi import WebSocket
from typing import List

class ConnectionController:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connections = {}

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

        connection_id = str(randint(10000, 99999))
        self.connections[websocket] = connection_id

    async def disconnect(self, websocket: WebSocket):
        await self.broadcast(websocket, "left the chat")
        self.active_connections.remove(websocket)
        del self.connections[websocket]

    async def get_message(self, websocket: WebSocket):
        message = await websocket.receive_text()
        return message

    async def broadcast(self, websocket: WebSocket, message: str):
        formated_msg = f"{self.connections[websocket]}: " + message

        for connection in self.active_connections:
            try:
                await connection.send_text(formated_msg)
            except RuntimeError:
                pass
