#!/bin/bash

# Build Flask API image
docker build -t client_data_project-flask_api:latest backend/

# Tag the Flask API image
docker tag client_data_project-flask_api:latest curvereality/client_data_project-flask_api:latest

# Push the Flask API image to Docker Hub
docker push curvereality/client_data_project-flask_api:latest

# Build Frontend image
docker build -t client_data_project-frontend:latest frontend/

# Tag the Frontend image
docker tag client_data_project-frontend:latest curvereality/client_data_project-frontend:latest

# Push the Frontend image to Docker Hub
docker push curvereality/client_data_project-frontend:latest