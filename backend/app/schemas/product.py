from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from backend.app.schemas.category import CategoryResponse


class ProductBase(BaseModel):
    name: str = Field(min_length=3, max_length=100, description='Product name')

    description: Optional[str] = Field(None, description='Product description')
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2, description='Product price (must be > 0)')
    category_id: int = Field(description='Category ID')
    image_url: Optional[str] = Field(None, max_length=500, description='Product image URL')


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int = Field(description='Unique product ID')

    created_at: datetime
    category: CategoryResponse = Field(description='Product category details')

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True
    )


class ProductListResponse(BaseModel):
    products: list[ProductResponse] = Field(description='List of products')
    total: int = Field(ge=0, description='Total number of products')
