from pydantic import BaseModel
import datetime
import db_dummy
from typing import List


class ReservaResumen(BaseModel):
    habitacion_id: str
    nombre: str
    fecha_inicio: str
    fecha_fin: str

    class Config:
        orm_mode = True


class ReservaIn(BaseModel):
    habitacion_id: str
    nombre: str
    fecha_inicio: str
    fecha_fin: str



