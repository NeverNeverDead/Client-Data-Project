#!/bin/bash

docker build -t client_data_project-flask_api:latest backend/

docker tag client_data_project-flask_api:latest curvereality/client_data_project-flask_api:latest

docker push curvereality/client_data_project-flask_api:latest

docker build -t client_data_project-frontend:latest frontend/

docker tag client_data_project-frontend:latest curvereality/client_data_project-frontend:latest

docker push curvereality/client_data_project-frontend:latest