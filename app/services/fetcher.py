import time
import pokebase as pb
from sqlalchemy.orm import Session
from models.pokemon_model import Pokemon

def fetch_and_store_pokemon_data(db: Session, count: int = 20):
    """
    Fetch Pokémon data using pokebase (auto-cached) and store it in SQLite DB.
    Respects fair use policy by leveraging caching and pacing requests.
    """
    for i in range(1, count + 1):
        # pokebase caches resources, reducing API load :contentReference[oaicite:1]{index=1}
        poke = pb.pokemon(i)
        
        types = ", ".join([t.type.name for t in poke.types])
        abilities = ", ".join([a.ability.name for a in poke.abilities])

        if not db.query(Pokemon).filter_by(id=poke.id).first():
            db.add(Pokemon(
                id=poke.id,
                name=poke.name,
                height=poke.height,
                weight=poke.weight,
                types=types,
                abilities=abilities
            ))
            db.commit()

        # Sleep briefly to avoid spamming API, respect fair use
        time.sleep(0.2)
