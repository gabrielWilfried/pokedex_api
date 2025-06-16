from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine, SessionLocal
from services.fetcher import fetch_and_store_pokemon_data
from api import pokemon

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pokemon.router, prefix="/api/pokemon", tags=["Pokemon"])

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    fetch_and_store_pokemon_data(db)
