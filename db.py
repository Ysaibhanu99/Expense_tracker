import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Create and return a connection to the Neon PostgreSQL database."""
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn


def init_db():
    """Create the expenses table if it doesn't already exist."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id       SERIAL PRIMARY KEY,
            title    VARCHAR(100)   NOT NULL,
            amount   DECIMAL(10, 2) NOT NULL,
            category VARCHAR(50)    NOT NULL,
            date     DATE           NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


# Run this file directly to create the table
if __name__ == "__main__":
    init_db()
    print("✅ Database table 'expenses' is ready.")
