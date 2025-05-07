# app/routes/message.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.message import MessageCreate, MessageOut
from app.crud import message as crud_message
from app.db.database import get_db
from app.models.room import RoomDB

router = APIRouter()

@router.post("/messages/", response_model=MessageOut)
def send_message(message: MessageCreate, db: Session = Depends(get_db)):
    # Verificar que la sala existe
    room = db.query(RoomDB).filter(RoomDB.id == message.room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="La sala no existe")

    return crud_message.create_message(db, message)

@router.get("/rooms/{room_id}/messages", response_model=list[MessageOut])
def get_room_messages(room_id: int, db: Session = Depends(get_db)):
    return crud_message.get_messages_by_room(db, room_id)
