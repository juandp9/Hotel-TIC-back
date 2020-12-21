import models
import db_dummy
from sqlalchemy.orm import Session
from db.entidades import Reserva

def obtener_reserva_por_id(db: Session, habitacion_id):
    return db.query(Reserva).et(reserva.habitacion_id)



def lista_reservas(db: Session):
    return db.query(Reserva).all()


def crear_reserva(db: Session, reserva: Reserva):
    if not db.query(Reserva).get(reserva.habitacion_id) is None:
        return False
    else:
        db.add(reserva)
        db.commit()
        return True


def lista_reservas_resumen():
    lista_reservas_resumen = []
    reservas = db_dummy.obtener_reserva()
    for habitacion_id, reserva in reservas.items():
        reserva_resumen = models.ReservaResumen(
            habitacio_id=reserva.habitacion_id, nombre=reserva.nombre)
        lista_reservas_resumen.append(reserva_resumen)
    return lista_reservas_resumen


def eliminar_reserva(db: Session, reserva: Reserva):
    if  db.query(Reserva).get(reserva.habitacion_id) is None:
        return False
    else:
        reserva = db.query(Reserva).get(reserva.habitacion_id)
        db.delete(reserva)
        db.commit()
        return True
