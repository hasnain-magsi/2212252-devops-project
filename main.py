from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/health")
def health_check():
   
    db_status = "Disconnected"
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "db"),
            database=os.getenv("POSTGRES_DB", "devops_db"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "postgres_pass"),
            connect_timeout=3
        )
        db_status = "Connected to Database"
        conn.close()
    except Exception:
        db_status = "Database connection failed"

    return {
        "status": "healthy",
        "student_registration_number": "2212252",
        "database": db_status
    }