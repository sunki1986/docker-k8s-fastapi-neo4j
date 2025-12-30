## DOCKER-FASTAPI-NEO4J Project
This project demonstrates a multi-service application featuring two FastAPI microservices interacting with a Neo4j graph database, sequentially deployed using both Docker Compose and Kubernetes (K8s). The repository structure is organized to showcase the configuration files and code for both deployment methods.
Table of Contents
Project Overview
Architecture
Local Deployment with Docker Compose
Deployment with Kubernetes
Project Structure

# 1. Project Overview
The main objective of this project was to build a robust backend system using Python's FastAPI framework and the Neo4j database, exploring different container orchestration solutions. It provides a clear, step-by-step guide for running the application using familiar tools like Docker Compose before migrating to a more scalable, production-ready Kubernetes environment.
# 2. Architecture
The application comprises three core services:
fastapi_app1: A Python FastAPI service.
fastapi_app2: A second Python FastAPI service.
neo4j: A Neo4j graph database instance for persistent storage.
All services are containerized using Docker, with configurations managed via YAML files.
# 3. Local Deployment with Docker Compose
This section outlines how to get the three services running locally using Docker Compose.
Prerequisites
Docker Desktop (includes Docker Engine and Docker Compose)
uv package manager (optional, used in this project)
Steps
Clone the Repository

bash
```
git clone 
```

bash
```
github.com
```

bash
```
cd DOCKER-FASTAPI-NEO4J
```

Configure Environment Variables
Create a .env file in the root directory based on a provided sample (if applicable), setting necessary variables like NEO4J_AUTH.
Run the Services
Use the provided docker-compose.yml file to start all three services.
bash
docker-compose up -d --build
Use code with caution.

Access the Application
The FastAPI documentation should be available at specified ports (e.g., http://localhost:8000/docs).
# 4. Deployment with Kubernetes
For a more scalable deployment, the project was migrated to Kubernetes. The K8s deployment uses specific manifests (.yaml files) for each service and configuration.
Prerequisites
A running Kubernetes cluster (e.g., Minikube, kind, or a cloud provider's cluster)
kubectl command-line tool
Steps
Review K8s Manifests
The necessary configuration files are located in the k8s/ directory and include deployments, services, secrets, and config maps.
Apply the Manifests
Deploy the services to your Kubernetes cluster using kubectl.
bash
kubectl apply -f k8s/
Use code with caution.

Verify Deployment
Check the status of your pods and services to ensure everything is running correctly.
bash
kubectl get pods,services
Use code with caution.

### 5. Project Structure
The repository maintains a clear structure, separating the application code from the deployment configurations.

.
├── .venv/                         # Virtual environment
├── fastapi_app1/                  # First FastAPI application
│   ├── Dockerfile                 
│   ├── main.py
│   └── pyproject.toml
├── fastapi_app2/                  # Second FastAPI application
│   ├── Dockerfile
│   ├── main.py
│   └── pyproject.toml
├── k8s/                           # Kubernetes configuration files
│   ├── fastapi_app1_deploy.yaml
│   ├── fastapi_app2_deploy.yaml
│   ├── neo4j-config.yaml
│   ├── neo4j-deployment.yaml
│   └── neo4j-secret.yaml
├── .env                           # Environment variables
├── .gitignore
├── .python-version
├── docker-compose.yml             # Docker Compose configuration file
├── README.md                      # This file
└── uv.lock