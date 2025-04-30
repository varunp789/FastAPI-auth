from pydantic import BaseModel, condecimal
from typing import Optional, List
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProductImageBase(BaseModel):
    image_url: str
    is_primary: bool = False

class ProductImageCreate(ProductImageBase):
    pass

class ProductImage(ProductImageBase):
    id: str
    product_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class ProductVariantBase(BaseModel):
    name: str
    price_adjustment: condecimal(max_digits=10, decimal_places=2) = 0
    stock_quantity: int = 0

class ProductVariantCreate(ProductVariantBase):
    pass

class ProductVariant(ProductVariantBase):
    id: str
    product_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: condecimal(max_digits=10, decimal_places=2)
    stock_quantity: int = 0
    category_id: str
    image_url: Optional[str] = None
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    category: Optional[Category] = None
    images: List[ProductImage] = []
    variants: List[ProductVariant] = []

    class Config:
        from_attributes = True 