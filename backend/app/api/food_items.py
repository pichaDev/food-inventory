from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.food_item import (
    FoodItemCreate,
    FoodItemResponse,
    FoodItemUpdate
)
from app.services.food_item_service import (
    get_food_items,
    create_food_item
)


router = APIRouter(
    prefix="/food-items",
    tags=["Food Items"]
)


@router.post("/", response_model=FoodItemResponse)
def create_food_item_endpoint(
    food_item: FoodItemCreate,
    db: Session = Depends(get_db)
):
    return create_food_item(
        db,
        food_item
    )


@router.get("/", response_model=list[FoodItemResponse])
def get_food_items_endpoint(
    db: Session = Depends(get_db)
):
    return get_food_items(db)


@router.get("/{food_item_id}", response_model=FoodItemResponse)
def get_food_item(
    food_item_id: int,
    db: Session = Depends(get_db)
):
    food_item = db.query(FoodItem).filter(
        FoodItem.id == food_item_id
    ).first()

    if not food_item:
        raise HTTPException(
            status_code=404,
            detail="Food item not found."
        )

    return food_item


@router.put("/{food_item_id}", response_model=FoodItemResponse)
def update_food_item(
    food_item_id: int,
    food_item_update: FoodItemUpdate,
    db: Session = Depends(get_db)
):
    food_item = db.query(FoodItem).filter(
        FoodItem.id == food_item_id
    ).first()

    if not food_item:
        raise HTTPException(
            status_code=404,
            detail="Food item not found."
        )

    update_data = food_item_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(food_item, key, value)

    db.commit()
    db.refresh(food_item)

    return food_item


@router.delete("/{food_item_id}")
def delete_food_item(
    food_item_id: int,
    db: Session = Depends(get_db)
):
    food_item = db.query(FoodItem).filter(
        FoodItem.id == food_item_id
    ).first()

    if not food_item:
        raise HTTPException(
            status_code=404,
            detail="Food item not found."
        )

    db.delete(food_item)
    db.commit()

    return {
        "message": "Food item deleted"
    }