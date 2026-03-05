from typing import Dict
from app.schemas.reserva import Reserva

# Diccionario en memoria para almacenar las reservas
reservas_db: Dict[int, Reserva] = {}
contador_reservas: int = 1