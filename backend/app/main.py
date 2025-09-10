from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title="FastAPI Vue SPA Boilerplate",
    description="A minimal but production-ready FastAPI + Vue SPA boilerplate",
    version="1.0.0",
)

# CORS middleware for Vue frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "FastAPI Vue SPA Boilerplate is running!"}