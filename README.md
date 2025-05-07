# 🗨️ Chat Service

This microservice, developed with **FastAPI** in Python, provides an interactive real-time chat system, enabling direct communication between users and a conversational bot powered by the **OpenAI API**.

---

## 🚀 Key Features

* 🟢 **Real-time Communication:** Implemented via WebSockets.
* 🤖 **Integrated OpenAI:** Utilizes advanced conversational models.
* 📂 **Data Persistence:** Uses PostgreSQL with asynchronous support.
* ⚙️ **Administrative Management:** User-friendly admin panel powered by SQLAdmin.
* 🔧 **Simple Configuration:** Managed through a `.env` file.
* 📐 **Efficient Migrations:** Version management with Alembic.

---

## 🧰 Tech Stack

| Technology    | Version  |
| ------------- | -------- |
| FastAPI       | 0.115.11 |
| Uvicorn       | 0.34.0   |
| SQLAlchemy    | 2.0.38   |
| AsyncPG       | 0.30.0   |
| Alembic       | 1.15.1   |
| psycopg2      | 2.9.9    |
| python-dotenv | 0.17.1   |
| Gunicorn      | 23.0.0   |
| Pydantic      | 2.10.6   |
| WebSockets    | 15.0.1   |
| SQLAdmin      | 0.20.1   |

---

## 📌 Installation and Execution Instructions

### 1️⃣ Clone the Repository

Clone the project from GitHub by executing:

```bash
git clone git@github.com:pablobn/chat-service.git
```

### 2️⃣ Run with Docker

Ensure Docker is installed and use `make` to manage the service:

```bash
make build  # Build the containers
make run    # Start the service
make down   # Stop and remove the containers
```

### 3️⃣ Configure Environment

Rename and modify the file `env.example` to `.env`, making sure to include your own OpenAI API key.

### 4️⃣ Test the Chat

After everything is up and running, open `test.html` to test the chat functionality.

### 5️⃣ Admin Panel

To view models and data, access the admin panel at:

```
localhost:8000/admin
```

### 6️⃣ API Documentation

To explore the API endpoints, visit:

```
localhost:8000/docs
```

---
