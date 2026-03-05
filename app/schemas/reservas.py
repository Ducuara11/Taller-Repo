from pydantic import BaseModel, Field
from datetime import datetime

class ReservaBase(BaseModel):
    sala: str = Field(..., example="Aula 101", description="La sala que será utilizada")
    usuario: str = Field(..., example="Juan Pérez", description="El usuario que realiza la reserva")
    fecha_horario: datetime = Field(..., example="2024-05-20T10:00:00", description="Fecha y horario de la reserva")
    asistentes: int = Field(..., gt=0, example=30, description="Número de personas que asistirán")
    estado: str = Field(default="Confirmada", example="Confirmada", description="El estado de la reserva")

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int

    class Config:
        from_attributes = True