from fastapi import APIRouter

from api.v1.routes import course

api_router = APIRouter()

api_router.include_router(
    course.router, prefix='/courses', tags=["courses"]
)
