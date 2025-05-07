from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.room import RoomCreate, RoomResponse
from app.db.database import get_db
from app.crud import room as crud  # Importar las funciones CRUD
router = APIRouter()

@router.post('/rooms', response_model=RoomResponse)
def create_room_handler(room: RoomCreate, db: Session = Depends(get_db)):
    """Crea una nueva sala en la base de datos"""
    db_room = crud.create_room(db, room)
    return db_room  # Devolvemos el objeto completo, no solo un mensaje

@router.get("/rooms/{room_id}", response_model=RoomResponse)
def get_room_handler(room_id: int, db: Session = Depends(get_db)):
    """Obtiene una sala por ID"""
    room = crud.get_room(db, room_id)
    if not room:
        return {"message": "Room not found"}
    return room  # Devuelve el objeto Room completo
