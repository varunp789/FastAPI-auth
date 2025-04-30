from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database
from .main import get_current_user

router = APIRouter(prefix="/api/admin", tags=["admin"])

async def get_admin_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform this action"
        )
    return current_user

# Category endpoints
@router.post("/categories", response_model=schemas.Category)
async def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/categories", response_model=List[schemas.Category])
async def list_categories(
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    return db.query(models.Category).all()

@router.put("/categories/{category_id}", response_model=schemas.Category)
async def update_category(
    category_id: str,
    category: schemas.CategoryCreate,
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    for key, value in category.dict().items():
        setattr(db_category, key, value)
    
    db.commit()
    db.refresh(db_category)
    return db_category

# Product endpoints
@router.post("/products", response_model=schemas.Product)
async def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products", response_model=List[schemas.Product])
async def list_products(
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    return db.query(models.Product).all()

@router.put("/products/{product_id}", response_model=schemas.Product)
async def update_product(
    product_id: str,
    product: schemas.ProductCreate,
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
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
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}

# Product Image endpoints
@router.post("/products/{product_id}/images", response_model=schemas.ProductImage)
async def add_product_image(
    product_id: str,
    image: schemas.ProductImageCreate,
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_image = models.ProductImage(**image.dict(), product_id=product_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

# Product Variant endpoints
@router.post("/products/{product_id}/variants", response_model=schemas.ProductVariant)
async def add_product_variant(
    product_id: str,
    variant: schemas.ProductVariantCreate,
    db: Session = Depends(database.get_db),
    admin: models.User = Depends(get_admin_user)
):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db_variant = models.ProductVariant(**variant.dict(), product_id=product_id)
    db.add(db_variant)
    db.commit()
    db.refresh(db_variant)
    return db_variant 