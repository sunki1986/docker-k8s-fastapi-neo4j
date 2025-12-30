from fastapi import FastAPI
from neo4j import GraphDatabase
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class Settings(BaseSettings):
    NEO4J_URI: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()

driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
)

app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "FastAPI 2 is running"}


@app.get("/neo4j-test")
def neo4j_test():
    with driver.session() as session:
        result = session.run("RETURN 'Neo4j connected!---------' AS msg")
        return {"neo4j_message": result.single()["msg"]}

# ----------------------------
# Models for creating nodes
# ----------------------------
class Person(BaseModel):
    name: str
    age: int

@app.post("/add-person")
def add_person(person: Person):
    with driver.session() as session:
        session.run(
            "CREATE (p:Person {name: $name, age: $age})",
            name=person.name,
            age=person.age
        )
    return {"message": f"Person {person.name} added successfully"}