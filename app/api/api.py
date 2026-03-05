from fastapi import APIRouter
from app.api.endpoints import reservas

api_router = APIRouter()
api_router.include_router(reservas.router, prefix="/reservas", tags=["reservas"])
