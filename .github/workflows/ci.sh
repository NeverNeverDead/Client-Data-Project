#!/bin/bash

# Компиляция Docker-образов
docker build -t client_data_project-backend:latest -f backend/Dockerfile .
docker build -t client_data_project-frontend:latest -f frontend/Dockerfile .

# Публикация образов в Docker Hub
docker push client_data_project-backend:latest
docker push client_data_project-frontend:latest
