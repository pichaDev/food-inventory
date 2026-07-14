from fastapi import FastAPI

from app.core.config import settings
from app.api import food_items


app = FastAPI(
    title=settings.app_name,
    version=settings.version
)


app.include_router(food_items.router)