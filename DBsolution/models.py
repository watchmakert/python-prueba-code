from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patente(Base):

    __tablename__ = "patentes"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    patente = Column(String(50))