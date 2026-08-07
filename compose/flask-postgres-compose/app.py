import os
import psycopg2
from flask import Flask

app = Flask(__name__)


def get_db_conn():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", ""),
        host=os.getenv("POSTGRES_HOST", "postgres"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
    )


def init_db():
    conn = get_db_conn()
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute("""
    CREATE TABLE IF NOT EXISTS hits (
      id INTEGER PRIMARY KEY,
      count BIGINT NOT NULL
    );
    """)
        cur.execute(
            "INSERT INTO hits (id, count) VALUES (1, 0) ON CONFLICT (id) DO NOTHING;"
        )
    conn.close()


init_db()


@app.route("/")
def hello():
    conn = get_db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO hits (id, count) VALUES (1, 1) ON CONFLICT (id) DO UPDATE SET count = hits.count + 1 RETURNING count;"
            )
            count = cur.fetchone()[0]
    conn.close()
    return f"Hello World from Docker! I have been seen {count} time(s).\n"
