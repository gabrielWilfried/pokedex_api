from pydantic import BaseModel, ConfigDict

class PokemonResponse(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    types: str
    abilities: str

    model_config = ConfigDict(from_attributes=True)