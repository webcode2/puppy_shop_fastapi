from app.core.config import Settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Replace "your_database.db" with your desired database filename
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:771531@localhost:5432/puppies"

engine = create_engine(Settings.DATABASE_CONNECTION_STRING)
print(Settings.ENV)
print(Settings.DATABASE_CONNECTION_STRING)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
