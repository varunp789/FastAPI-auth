from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dependencies import get_current_admin_user
from app.db.session import get_db
from app.models.user import User
from app.models.product import Category, Product, ProductImage, ProductVariant
from app.schemas.product import (
    CategoryCreate, Category as CategorySchema,
    ProductCreate, Product as ProductSchema,
    ProductImageCreate, ProductImage as ProductImageSchema,
    ProductVariantCreate, ProductVariant as ProductVariantSchema
)

router = APIRouter()

# Category endpoints
@router.post("/categories", response_model=CategorySchema)
async def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/categories", response_model=List[CategorySchema])
async def list_categories(
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    return db.query(Category).all()

@router.put("/categories/{category_id}", response_model=CategorySchema)
async def update_category(
    category_id: str,
    category: CategoryCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    for key, value in category.dict().items():
        setattr(db_category, key, value)
    
    db.commit()
    db.refresh(db_category)
    return db_category

# Product endpoints
@router.post("/products", response_model=ProductSchema)
async def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products", response_model=List[ProductSchema])
async def list_products(
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    return db.query(Product).all()

@router.put("/products/{product_id}", response_model=ProductSchema)
async def update_product(
    product_id: str,
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.dict().items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/products/{product_id}")
async def delete_product(
    product_id: str,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

# Product Image endpoints
@router.post("/products/{product_id}/images", response_model=ProductImageSchema)
async def add_product_image(
    product_id: str,
    image: ProductImageCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_image = ProductImage(**image.dict(), product_id=product_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# Product Variant endpoints
@router.post("/products/{product_id}/variants", response_model=ProductVariantSchema)
async def add_product_variant(
    product_id: str,
    variant: ProductVariantCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin_user)
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_variant = ProductVariant(**variant.dict(), product_id=product_id)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant 