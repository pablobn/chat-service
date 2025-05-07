from sqlalchemy.orm import Session
from app.schemas.room import RoomCreate
from app.models.room import RoomDB  # Modelo SQLAlchemy

def create_room(db: Session, room: RoomCreate):
    """Crea una nueva sala en la base de datos"""
    db_room = RoomDB(name=room.name)  # Convertimos el esquema Pydantic a SQLAlchemy
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_room(db: Session, room_id: int):
    """Obtiene una sala por ID"""
    return db.query(RoomDB).filter(RoomDB.id == room_id).first()
