from datetime import date

from sqlalchemy import String, Float, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class FoodItem(Base):
    __tablename__ = "food_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    quantity: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    category: Mapped[str | None] = mapped_column(
        String(50)
    )

    location: Mapped[str | None] = mapped_column(
        String(50)
    )

    purchase_date: Mapped[date | None] = mapped_column(
        Date
    )

    expiration_date: Mapped[date | None] = mapped_column(
        Date
    )

    notes: Mapped[str | None] = mapped_column(
        Text
    )