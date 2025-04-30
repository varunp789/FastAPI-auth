from sqlalchemy import create_engine
from app.core.config import settings
from app.db.base import Base
from app.models.user import User
from app.models.product import Category, Product, ProductImage, ProductVariant

def init_db():
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    Base.metadata.drop_all(bind=engine)  # Drop all tables
    Base.metadata.create_all(bind=engine)  # Create all tables

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully!") 