from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field(description='Product ID')
    quantity: int = Field(gt=0, description='Quantity (must be > 0)')


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(description='Product ID')
    quantity: int = Field(gt=0, description='New quantity (must be > 0)')


class CartItem(CartItemBase):
    name: str = Field(min_length=2, max_length=100, description='Product name')
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2, description='Product price')
    subtotal: Decimal = Field(ge=0, max_digits=10, decimal_places=2,
                              description='Total price for this item (price * quantity)')
    image_url: Optional[str] = Field(None, max_length=500, description='Product image URL')

    model_config = ConfigDict(from_attributes=True)


class CartResponse(BaseModel):
    items: list[CartItem] = Field(default_factory=list, description='List of items in cart')
    total: Decimal = Field(ge=0, max_digits=10, decimal_places=2, description='Total cart price')
    items_count: int = Field(ge=0, description='Total number of items in cart')

    model_config = ConfigDict(from_attributes=True)
