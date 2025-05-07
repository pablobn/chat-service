from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class RoomDB(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Relación con mensajes
    messages = relationship("MessageDB", back_populates="room", cascade="all, delete-orphan")
