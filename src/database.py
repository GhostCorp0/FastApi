from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine


DATABASE_URL = "postgresql://fastapi_db_ino9_user:I5r3OIMQGKb6OZePd4xdEcV8ASems9py@dpg-d6aruf6mcj7s73elb61g-a/fastapi_db_ino9"

engine =   create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()