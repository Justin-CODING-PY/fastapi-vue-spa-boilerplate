from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint - similar to Django version
    This endpoint can be called by the Vue frontend to verify API connectivity
    """
    return {
        "status": "healthy",
        "message": "FastAPI backend is running",
        "environment": settings.ENVIRONMENT,
        "version": settings.VERSION
    }

@router.get("/ping")
async def ping():
    """
    Simple ping endpoint
    """
    return {"message": "pong"}