# FastAPI Authentication Demo

This is a FastAPI project with PostgreSQL integration and JWT authentication.

## Setup Instructions

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following content:
```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Create the PostgreSQL database:
```bash
createdb dbname
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- POST /api/register - Register a new user
- POST /api/login - Login and get JWT token
- GET /api/users/me - Get current user info (protected route)

## Features

- User registration and login
- JWT token authentication
- PostgreSQL database integration
- Password hashing
- Protected routes 