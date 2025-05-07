# Makefile actualizado

# Definición de colores
YELLOW := $(shell printf '\033[33m')
RED := $(shell printf '\033[31m')
GREEN := $(shell printf '\033[32m')
CYAN := $(shell printf '\033[36m')
RESET := $(shell printf '\033[0m')

# Archivo docker-compose
DCFILE := srcs/docker-compose.yml

# Detectar si se usa 'docker compose' o 'docker-compose'
ifeq ($(shell docker compose version >/dev/null 2>&1 && echo "docker compose"),docker compose)
    DC := docker compose -f $(DCFILE)
else
    DC := docker-compose -f $(DCFILE)
endif

# Directorio del proyecto
PROJECTFOLDER := $(shell pwd)

# Objetivos principales
all: run

# Construcción usando el caché
build:
	@printf "$(YELLOW)██████████████████████ Building Project Containers ███████████████████████$(RESET)\n"
	@test -d $(PROJECTFOLDER)/srcs/db-storage || mkdir -p $(PROJECTFOLDER)/srcs/db-storage
	@$(DC) build
	@printf "$(GREEN)████████████████████████ Build Project is DONE █████████████████████████$(RESET)\n"
	@$(MAKE) run

run:
	@printf "$(YELLOW)██████████████████████ Running Project Containers ██████████████████████$(RESET)\n"
	@$(DC) up -d
	@printf "$(GREEN)██████████████████████ Project is up and running ██████████████████████$(RESET)\n"

stop:
	@printf "$(RED)██████████████████████ Stopping Project Containers █████████████████████$(RESET)\n"
	@$(DC) stop
	@printf "$(GREEN)████████████████████████ Project is stopped ███████████████████████████$(RESET)\n"

down:
	@printf "$(RED)██████████████████████ Removing Project Containers █████████████████████$(RESET)\n"
	@$(DC) down -v
	@printf "$(GREEN)████████████████████████ Project is down ██████████████████████████████$(RESET)\n"

clean:
	@printf "$(RED)██████████████████████ Cleaning Docker System █████████████████████$(RESET)\n"
	@docker system prune -a --volumes -f
	@printf "$(GREEN)████████████████████████ Docker system is cleaned ███████████████████████████$(RESET)\n"

re: down build run

status:
	@printf "$(CYAN)██████████████████████ Checking Project Status █████████████████████$(RESET)\n"
	@$(DC) ps

logs:
	@printf "$(CYAN)██████████████████████ Showing Project Logs █████████████████████$(RESET)\n"
	@$(DC) logs -f

# Opciones adicionales
MAKEFLAGS += --warn-undefined-variables

# Declaraciones .PHONY agrupadas al final
.PHONY: all build build-nocache run stop down clean re status logs
