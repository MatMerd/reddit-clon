from fastapi import APIRouter

from app.api.api_v1.endpoints import health_check


api_router = APIRouter()

api_router.include_router(health_check.router, prefix="/health", tags=["health"])
