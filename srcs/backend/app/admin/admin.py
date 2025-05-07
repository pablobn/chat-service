from sqladmin import Admin, ModelView
from app.db.database import engine
from fastapi import FastAPI
from app.models.room import RoomDB
from app.models.message import MessageDB

# Crear la instancia de Admin
def setup_admin(app: FastAPI):
    admin = Admin(app, engine)

    # Agregar vistas de administración
    class RoomAdmin(ModelView, model=RoomDB):
        column_list = [RoomDB.id, RoomDB.name]  # Columnas visibles en el panel
    
    class MessageAdmin(ModelView, model=MessageDB):
        column_list = [MessageDB.id, MessageDB.room_id, MessageDB.content]

    admin.add_view(RoomAdmin)
    admin.add_view(MessageAdmin)

    return admin
