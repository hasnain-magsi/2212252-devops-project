from fastapi import FastAPI
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(
    title="SZABIST DevOps Final Project",
    description="Automated CI/CD Deployment Pipeline via GitHub Actions to AWS EC2",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {
        "status": "Success",
        "message": "Welcome to my SZABIST DevOps Final Project Live on AWS!",
        "environment": "Docker Container",
        "pipeline": "GitHub Actions CI/CD"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "configured"}


@app.get("/db-test")
def test_db_connection():
    try:
        # Pulls from standard Docker environment variables
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database=os.getenv("DB_NAME", "postgres"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "password"),
            cursor_factory=RealDictCursor
        )
        connection.close()
        return {"database_status": "Connected successfully to PostgreSQL!"}
    except Exception as e:
        return {"database_status": "Disconnected", "error": str(e)}