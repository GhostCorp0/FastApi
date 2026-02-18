from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine


DATABASE_URL = "postgresql://user:Download%401234@localhost:5432/fastapi_db"

engine =   create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()