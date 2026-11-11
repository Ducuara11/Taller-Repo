from fastapi import APIRouter, HTTPException
from typing import List, Dict
from app.schemas.reservas import Reserva, ReservaCreate
from app.db.store import reservas_db
import app.db.store as store

router = APIRouter()

@router.post("/", response_model=Dict[str, str], status_code=201)
def crear_reserva(reserva_in: ReservaCreate):
    reserva_id = store.contador_reservas
    
    # Crear la reserva con el ID asignado
    nueva_reserva = Reserva(id=reserva_id, **reserva_in.model_dump())
    
    reservas_db[reserva_id] = nueva_reserva
    store.contador_reservas += 1
    
    return {"mensaje": "Reserva creada exitosamente", "id_reserva": str(reserva_id)}

@router.get("/", response_model=List[Reserva])
def obtener_todas_las_reservas():
    return list(reservas_db.values())

@router.get("/{reserva_id}", response_model=Reserva)
def obtener_reserva(reserva_id: int):
    if reserva_id not in reservas_db:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reservas_db[reserva_id]
