from datetime import date

from pydantic import BaseModel


class FoodItemCreate(BaseModel):
    name: str
    quantity: float
    unit: str
    category: str | None = None
    location: str | None = None
    purchase_date: date | None = None
    expiration_date: date | None = None
    notes: str | None = None


class FoodItemResponse(FoodItemCreate):
    id: int

    class Config:
        from_attributes = True


class FoodItemUpdate(BaseModel):
    name: str | None = None
    quantity: float | None = None
    unit: str | None = None
    category: str | None = None
    location: str | None = None
    purchase_date: date | None = None
    expiration_date: date | None = None
    notes: str | None = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "quantity": 1,
                "notes": "Opened"
            }
        }
    }