from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import auth, admin
from app.db.base import Base
from app.db.session import engine

# Print environment variables (remove in production)
print("Database URL:", settings.SQLALCHEMY_DATABASE_URI)
print("Secret Key:", settings.SECRET_KEY[:10] + "..." if settings.SECRET_KEY else "Not set")

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# Include routers
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(admin.router, prefix=f"{settings.API_V1_STR}/admin", tags=["admin"]) 


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

