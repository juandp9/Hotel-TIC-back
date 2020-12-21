from pydantic import BaseModel
import datetime
from typing import Dict



class Reserva(BaseModel):
    habitacion_id: str
    nombre: str
    fecha_inicio: str
    fecha_fin: str


reservas: Dict[str, Reserva]

reservas = { 
    "1": Reserva(habitacion_id="1",nombre="diego",fecha_inicio="2020-12-24",fecha_fin="2021-01-14"),
    "2": Reserva(habitacion_id="2",nombre="daniel",fecha_inicio="2020-12-24",fecha_fin="2021-01-15"),
}



def obtener_lista_reservas():
    lista_reservas=[]
    for reserva in reservas:
        lista_reservas.append(reservas[reserva])
        
    return lista_reservas



def obtener_reserva(habitacion_id: int):
    if habitacion_id in Reserva:
        return Reserva(habitacion_id)
    else:
        return None

def crear_reserva(reserva: Reserva):
    if  reserva.habitacion_id in reservas:
        return False
    else:
        reserva[reserva.habitacion_id] = reserva
        return True

def eliminar_reserva(reserva: Reserva):
    if reserva.habitacion_id in reservas:
        del reserva[reserva.habitacion_id] 
        return True
    else:
        return False