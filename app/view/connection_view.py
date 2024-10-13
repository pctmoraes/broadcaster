from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from app.controller.connection_controller import ConnectionController

connection = ConnectionController()
route = APIRouter()

@route.websocket("/broadcaster/chat")
async def websocket_endpoint(websocket: WebSocket):
    await connection.connect(websocket)
    try:
        while True:
            message = await connection.get_message(websocket)
            await connection.broadcast(websocket, message)
    except WebSocketDisconnect:
        await connection.disconnect(websocket)
