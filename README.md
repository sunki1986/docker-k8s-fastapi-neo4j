# FastAPI + Neo4j Project

This project contains:

- FastAPI backend with Neo4j database
- Dockerized using Docker Compose
- Uses `uv` for dependency management
- Endpoints:
  - GET `/ping` → test FastAPI
  - GET `/neo4j-test` → test Neo4j connectivity
  - POST `/add-person` → insert person node
