from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from todo.core.config import settings

engine = create_engine(settings.db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
