from fastapi import WebSocket, WebSocketDisconnect
import json
from typing import Dict, List
from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError
from sqlalchemy.orm import Session

from app.crud.room import get_room
from app.crud import message as crud_message
from app.schemas.message import MessageCreate
from app.db.database import SessionLocal

# Diccionario para manejar las conexiones activas en las salas de chat
active_connections: Dict[int, List[WebSocket]] = {}

async def websocket_endpoint(room_id: int, websocket: WebSocket):
    """Maneja las conexiones WebSocket para una sala de chat."""

    # Crear una sesión de base de datos para validar la sala
    db: Session = SessionLocal()
    room = get_room(db, room_id)
    db.close()

    # Si la sala no existe, cerrar la conexión
    if not room:
        await websocket.close()
        return

    # Aceptar la conexión
    await websocket.accept()

    # Agregar la conexión al diccionario de conexiones activas
    if room_id not in active_connections:
        active_connections[room_id] = []
    active_connections[room_id].append(websocket)

    try:   
        while True:
            message = await websocket.receive_text()

            db = SessionLocal()
            msg_schema = MessageCreate(content=message, room_id=room_id)
            crud_message.create_message(db, msg_schema)
            db.close()

            message_data = {
                "room_id": room_id,
                "message": message,
            }
            json_message = json.dumps(message_data)

            for connection in active_connections[room_id]:
                if connection != websocket:
                    await connection.send_text(json_message)

    except WebSocketDisconnect:
        print(f"Cliente desconectado de la sala {room_id}")

    finally:
        if room_id in active_connections:
            active_connections[room_id].remove(websocket)
            if not active_connections[room_id]:
                del active_connections[room_id]