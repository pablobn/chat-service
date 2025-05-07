from fastapi import WebSocket, WebSocketDisconnect
import json
from typing import Dict, List
from sqlalchemy.orm import Session

from app.crud.room import get_room
from app.crud import message as crud_message
from app.schemas.message import MessageCreate
from app.db.database import SessionLocal

from app.services.chatgpt import get_chatgpt_response

# Diccionario global para mantener las conexiones activas
active_connections: Dict[int, List[WebSocket]] = {}

async def websocket_chatgpt_endpoint(room_id: int, websocket: WebSocket):
    db: Session = SessionLocal()
    room = get_room(db, room_id)
    db.close()

    if not room:
        await websocket.close()
        return

    await websocket.accept()

    if room_id not in active_connections:
        active_connections[room_id] = []
    active_connections[room_id].append(websocket)

    try:
        while True:
            message = await websocket.receive_text()

            # Guardar mensaje del usuario
            db = SessionLocal()
            msg_schema = MessageCreate(content=message, room_id=room_id)
            crud_message.create_message(db, msg_schema)
            db.close()

            user_msg = json.dumps({
                "room_id": room_id,
                "message": message,
                "from": "user"
            })
            for connection in active_connections[room_id]:
                await connection.send_text(user_msg)

            # Obtener respuesta de ChatGPT
            chatgpt_response = await get_chatgpt_response(message)

            # Guardar respuesta de ChatGPT
            db = SessionLocal()
            msg_schema_bot = MessageCreate(content=chatgpt_response, room_id=room_id)
            crud_message.create_message(db, msg_schema_bot)
            db.close()

            bot_msg = json.dumps({
                "room_id": room_id,
                "message": chatgpt_response,
                "from": "ChatGPT"
            })
            for connection in active_connections[room_id]:
                await connection.send_text(bot_msg)

    except WebSocketDisconnect:
        print(f"Cliente desconectado de la sala {room_id}")

    finally:
        if room_id in active_connections:
            active_connections[room_id].remove(websocket)
            if not active_connections[room_id]:
                del active_connections[room_id]
