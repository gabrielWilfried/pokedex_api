from sqlalchemy import Column, Integer, String
from db.database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    height = Column(Integer)
    weight = Column(Integer)
    types = Column(String)
    abilities = Column(String)