from db.conexion_db import Base, motor
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class Reserva(Base):
    __tablename__ = "reservacion"
    habitacion_id = Column(String, primary_key=True)
    nombre = Column(String)
    fecha_inicio = Column(String)
    fecha_fin = Column(String)
    


Base.metadata.create_all(bind=motor)
