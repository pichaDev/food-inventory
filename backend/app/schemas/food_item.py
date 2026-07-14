from datetime import date, datetime

from pydantic import BaseModel


class FoodItemCreate(BaseModel):
    name: str
    brand: str | None = None
    quantity: float
    unit: str
    category: str | None = None
    location: str | None = None
    purchase_date: date | None = None
    expiration_date: date | None = None
    notes: str | None = None


class FoodItemResponse(FoodItemCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class FoodItemUpdate(BaseModel):
    name: str | None = None
    brand: str | None = None
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