from fastapi import APIRouter
from app.db.database import Base

router = APIRouter()

@router.get("/db/tables")
def get_tables():
    return {"tables": list(Base.metadata.tables.keys())}
