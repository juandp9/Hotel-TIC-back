from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


motor = create_engine(
    "postgresql://postgres:juan@localhost:5432/Hotel_TIC")

Sesion = sessionmaker(bind=motor, autocommit=False, autoflush=False)


def obtener_db():
    sesion = Sesion()
    try:
        yield sesion
    finally:
        sesion.close()


Base = declarative_base()
Base.metadata.schema = "reservas"
