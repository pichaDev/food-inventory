from datetime import date, datetime

from pydantic import BaseModel, Field


class FoodItemCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100
    )

    brand: str | None = Field(
        default=None,
        max_length=50
    )

    quantity: float = Field(
        ge=0
    )

    unit: str = Field(
        min_length=1,
        max_length=20
    )

    category: str | None = Field(
        default=None,
        max_length=50
    )

    location: str | None = Field(
        default=None,
        max_length=50
    )

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
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    brand: str | None = Field(
        default=None,
        max_length=50
    )

    quantity: float | None = Field(
        default=None,
        ge=0
    )

    unit: str | None = Field(
        default=None,
        min_length=1,
        max_length=20
    )

    category: str | None = Field(
        default=None,
        max_length=50
    )

    location: str | None = Field(
        default=None,
        max_length=50
    )

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