from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "postgresql://postgres:password@localhost:5432/critical_path_db"
# changing the url to match the one in docker-compose.yml later on
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False,
    bind=engine
    )
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()