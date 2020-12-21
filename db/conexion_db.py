from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


motor = create_engine(
    "postgres://okgdvcnharanca:e88a3e4ce65f07b51ee536e8365b6e2d31b28a67456077ed82f925deef29715f@ec2-3-229-51-131.compute-1.amazonaws.com:5432/d7383bl3fnq77")

Sesion = sessionmaker(bind=motor, autocommit=False, autoflush=False)


def obtener_db():
    sesion = Sesion()
    try:
        yield sesion
    finally:
        sesion.close()


Base = declarative_base()
Base.metadata.schema = "reservas"
