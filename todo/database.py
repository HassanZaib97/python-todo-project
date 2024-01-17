from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Any

# Replace the connection details with your Neon database information
SQLALCHEMY_DATABASE_URL = "postgresql://HassanZaib97:31xHIgsSrqFB@ep-winter-shadow-01178524.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print(SessionLocal)

Base: Any = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)  # Add this line
    description = Column(String)

# Create the table
Base.metadata.create_all(bind=engine)
