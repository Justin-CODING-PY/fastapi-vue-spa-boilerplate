from typing import List
from decouple import config

class Settings:
    # Basic settings
    PROJECT_NAME: str = "FastAPI Vue SPA Boilerplate"
    VERSION: str = "1.0.0"
    
    # Environment
    ENVIRONMENT: str = config("ENVIRONMENT", default="development")
    DEBUG: bool = config("DEBUG", default=True, cast=bool)
    
    # Security
    SECRET_KEY: str = config("SECRET_KEY", default="your-secret-key-change-this-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=30, cast=int)
    ALGORITHM: str = "HS256"
    
    # Database
    DATABASE_URL: str = config("DATABASE_URL", default="postgresql://user:password@localhost/dbname")
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = config(
        "BACKEND_CORS_ORIGINS",
        default="http://localhost:3000,http://localhost:5173",
        cast=lambda v: [i.strip() for i in v.split(",")]
    )

settings = Settings()