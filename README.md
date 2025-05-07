# 🗨️ chat-service

This microservice, built with **FastAPI** in Python, implements a chat system that enables real-time interaction between users and a conversational bot powered by the **OpenAI API**.

## 🚀 Features

- Real-time chat via WebSockets
- Integration with OpenAI's conversational models
- PostgreSQL database with async support
- Admin panel powered by SQLAdmin
- Environment configuration with `.env`
- Migrations handled with Alembic

## 🧰 Tech Stack

- **FastAPI** `0.115.11`
- **Uvicorn** `0.34.0`
- **SQLAlchemy** `2.0.38`
- **AsyncPG** `0.30.0`
- **Alembic** `1.15.1`
- **psycopg2** `2.9.9`
- **python-dotenv** `0.17.1`
- **Gunicorn** `23.0.0`
- **Pydantic** `2.10.6`
- **WebSockets** `15.0.1`
- **SQLAdmin** `0.20.1`

## ⚙️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/chat-service.git
cd chat-service
