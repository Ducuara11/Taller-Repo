from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.api import api_router

app = FastAPI(
    title="Sistema de Reservas de Salas",
    description="Servicio web para registrar y consultar reservas de salas académicas.",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")