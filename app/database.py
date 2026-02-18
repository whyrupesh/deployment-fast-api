from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import AsyncGenerator
import os
from dotenv import load_dotenv

load_dotenv()

from urllib.parse import quote_plus

# Construct Database URL from individual env vars if DATABASE_URL not set
# Prefer AsyncPG driver: postgresql+asyncpg://user:password@host:port/dbname
def get_env(key):
    val = os.getenv(key)
    return val.strip('"').strip("'") if val else None

DB_USER = get_env("SUPABASE_DB_USER")
DB_PASSWORD = get_env("SUPABASE_DB_PASSWORD")
DB_HOST = get_env("SUPABASE_DB_HOST")
DB_PORT = get_env("SUPABASE_DB_PORT")
DB_NAME = get_env("SUPABASE_DB_NAME")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL and all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
     encoded_user = quote_plus(DB_USER)
     encoded_password = quote_plus(DB_PASSWORD)
     DATABASE_URL = f"postgresql+asyncpg://{encoded_user}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}?ssl=require"
elif DATABASE_URL:
     if not DATABASE_URL.startswith("postgresql+asyncpg"):
         DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
     if "ssl=" not in DATABASE_URL:
         separator = "&" if "?" in DATABASE_URL else "?"
         DATABASE_URL += f"{separator}ssl=require"


if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set and could not be constructed.")

engine = create_async_engine(
    DATABASE_URL,
    echo=False, # Set to True for SQL logging
    future=True,
    connect_args={
        "statement_cache_size": 0
    }
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
