#!/bin/sh

# Función para esperar a que la base de datos esté lista
wait_for_postgres() {
  STATUS=1
  echo "Waiting for PostgreSQL to be ready..."
  while [ $STATUS -ne 0 ]; do
    pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER
    STATUS=$?
    if [ $STATUS -eq 0 ]; then
      echo "PostgreSQL is ready!"
    else
      sleep 1
    fi
  done
}

# Función para aplicar migraciones con Alembic
run_migrations() {
  echo "Running database migrations..."
  alembic upgrade head
}

# Función para iniciar el servidor con Uvicorn
start_server() {
  echo "Starting FastAPI server..."
  uvicorn app.main:app --host 0.0.0.0 --port 8004 --reload
}

# Ejecutar las funciones
wait_for_postgres
run_migrations
start_server
