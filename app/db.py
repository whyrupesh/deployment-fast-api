import psycopg2
import os
from psycopg2.extras import RealDictCursor

# DB_CONFIG = {
#     "dbname": "fundizr",
#     "user": "rupesh",
#     "host": "localhost",
#     "port": 5432
# }

DB_CONFIG = {
    "dbname": os.getenv("SUPABASE_DB_NAME"),
    "user": os.getenv("SUPABASE_DB_USER"),
    "host": os.getenv("SUPABASE_DB_HOST"),
    "port": os.getenv("SUPABASE_DB_PORT"),
    "password": os.getenv("SUPABASE_DB_PASSWORD"),
    "sslmode": "require"
}


# def get_db():
#     return psycopg2.connect(
#         host=os.getenv("SUPABASE_DB_HOST"),
#         port=os.getenv("SUPABASE_DB_PORT"),
#         dbname=os.getenv("SUPABASE_DB_NAME"),
#         user=os.getenv("SUPABASE_DB_USER"),
#         password=os.getenv("SUPABASE_DB_PASSWORD"),
#         sslmode="require",
#     )

def get_connection():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
