import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """Create and return a connection to the Neon PostgreSQL database."""
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return conn
    except psycopg2.OperationalError as e:
        print(f"❌ Database connection failed: {e}")
        raise
    except Exception as e:
        print(f"❌ Unexpected error connecting to database: {e}")
        raise


def init_db():
    """Create the expenses table if it doesn't already exist."""
    try:
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
        print("✅ Database table 'expenses' is ready.")
    except Exception as e:
        print(f"❌ Failed to initialize database: {e}")
        raise


# Run this file directly to create the table
if __name__ == "__main__":
    init_db()
