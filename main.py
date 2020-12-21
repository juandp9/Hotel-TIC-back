from typing import List
from fastapi import Depends, FastAPI, HTTPException
import models
import repositorio
import db_dummy
import db
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.conexion_db import obtener_db
from db.entidades import Reserva

app=FastAPI()
origins=[
    "https://hotel-tic-front.herokuapp.com/", "http//localhost",
]

app.add_middleware(
    CORSMiddleware,allow_origins=origins,
    allow_credentials=True, allow_methods=["*"],allow_headers=["*"],
)

@app.get("/reservas/ver-reservas", response_model=List[models.ReservaResumen])
async def obtener_lista_reservas(db: Session = Depends(obtener_db)):
    return repositorio.lista_reservas(db)

@app.post("/reservas/crear/")
async def crear_reserva(reserva: db_dummy.Reserva, db: Session = Depends(obtener_db)):

    operacion_exitosa = repositorio.crear_reserva(
        db, Reserva(**reserva.dict()))
    if operacion_exitosa:
        return {"mensaje": "reserva creada correctamente"}
    else:
        raise HTTPException(
            status_code=400, detail="Reserva no pudo ser creada")

@app.delete("/reservas/eliminar")
async def eliminar_reserva(reserva: db_dummy.Reserva, db: Session = Depends(obtener_db)):
    operacion_exitosa = repositorio.eliminar_reserva(
        db, Reserva(**reserva.dict()))
    if operacion_exitosa:
        return {"mensaje": "reserva eliminada correctamente"}
    else:
        raise HTTPException(
            status_code=400, detail="Reserva no pudo ser eliminada")
