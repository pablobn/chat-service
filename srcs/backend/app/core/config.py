import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env

class Settings:
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")

settings = Settings()
