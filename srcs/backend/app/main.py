from fastapi import FastAPI
from app.routes import room, db, message
from app.admin.admin import setup_admin
from app.websockets.handlers import websocket_endpoint
from fastapi.middleware.cors import CORSMiddleware
from app.websockets.chatgpt_handler import websocket_chatgpt_endpoint

app = FastAPI(title="Chat Microservice")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ¡Peligroso en producción!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas REST
app.include_router(room.router, prefix="/chat", tags=["Rooms"])
app.include_router(message.router, prefix="/chat", tags=["Messages"])
app.include_router(db.router, prefix="")

# Incluir panel de administración
setup_admin(app)

# Agregar WebSockets
app.add_api_websocket_route("/messages/{room_id}", websocket_endpoint)
app.add_api_websocket_route("/chatgpt/{room_id}", websocket_chatgpt_endpoint)

@app.get("/")
def root():
    return {"message": "Microservicio FastAPI con WebSockets funcionando 🚀"}
