from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import FoodItem
from app.schemas.food_item import FoodItemCreate, FoodItemResponse


router = APIRouter(
    prefix="/food-items",
    tags=["Food Items"]
)


@router.post("/", response_model=FoodItemResponse)
def create_food_item(
    food_item: FoodItemCreate,
    db: Session = Depends(get_db)
):
    db_food_item = FoodItem(**food_item.model_dump())

    db.add(db_food_item)
    db.commit()
    db.refresh(db_food_item)

    return db_food_item