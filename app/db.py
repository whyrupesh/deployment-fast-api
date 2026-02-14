import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "fundizr",
    "user": "rupesh",
    "host": "localhost",
    "port": 5432
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
