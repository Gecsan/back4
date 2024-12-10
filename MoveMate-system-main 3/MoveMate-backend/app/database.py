from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL Configuration  for PostgreSQL -- I'm using a local DB
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0000@localhost/movemate"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()


#  provide a database session in each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()