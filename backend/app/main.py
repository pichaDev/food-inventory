from fastapi import FastAPI

from app.core.config import settings
from app.db.database import engine
from app.db.models import Base
from app.api import food_items


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.app_name,
    version=settings.version
)


app.include_router(food_items.router)

@app.get("/")
def root():
    return {
        "message": "Hello, Foodery!"
    }