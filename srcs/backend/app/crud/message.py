from sqlalchemy.orm import Session
from app.models.message import MessageDB
from app.schemas.message import MessageCreate

def create_message(db: Session, message: MessageCreate):
    """Crea un nuevo mensaje en la base de datos"""
    db_message = MessageDB(**message.dict())  # Convierte el schema Pydantic a modelo SQLAlchemy
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages_by_room(db: Session, room_id: int):
    """Obtiene todos los mensajes de una sala ordenados por fecha"""
    return db.query(MessageDB)\
             .filter(MessageDB.room_id == room_id)\
             .order_by(MessageDB.timestamp)\
             .all()

def get_message(db: Session, message_id: int):
    """Obtiene un mensaje concreto por su ID"""
    return db.query(MessageDB).filter(MessageDB.id == message_id).first()
