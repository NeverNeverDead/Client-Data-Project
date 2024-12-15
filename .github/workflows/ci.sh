#!/bin/bash

docker build -t client_data_project-frontend:latest ./frontend
docker build -t client_data_project-flask_api:latest ./backend

docker push client_data_project-frontend:latest
docker push client_data_project-flask_api:latest
