from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.models import Base


DATABASE_URL = "postgresql://foodery:foodery@localhost:5432/foodery"


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

Base.metadata.create_all(bind=engine)