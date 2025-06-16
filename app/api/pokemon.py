from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.pokemon_model import Pokemon
from schemas.pokemon_schema import PokemonResponse
from typing import List

router = APIRouter()

@router.get("/", response_model=List[PokemonResponse])
def get_pokemons(db: Session = Depends(get_db)):
    return db.query(Pokemon).all()

