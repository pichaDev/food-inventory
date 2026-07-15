from sqlalchemy.orm import Session

from app.db.models import FoodItem
from app.schemas.food_item import FoodItemCreate


def get_food_items(
    db: Session
):
    return db.query(FoodItem).all()


def create_food_item(
    db: Session,
    food_item: FoodItemCreate
):
    db_food_item = FoodItem(
        **food_item.model_dump()
    )

    db.add(db_food_item)
    db.commit()
    db.refresh(db_food_item)

    return db_food_item