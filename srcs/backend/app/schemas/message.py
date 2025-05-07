# app/schemas/message.py
from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    content: str
    room_id: int

class MessageOut(BaseModel):
    id: int
    content: str
    timestamp: datetime
    room_id: int

    class Config:
        orm_mode = True
