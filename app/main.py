from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from db.database import Base, engine, SessionLocal
from services.fetcher import fetch_and_store_pokemon_data
from api import pokemon

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(pokemon.router, prefix="/api/pokemon", tags=["Pokemon"])

@app.get("/")
async def root():
    return {"message": "Welcome to PokePipeline API. Visit /docs for API documentation."}

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    fetch_and_store_pokemon_data(db)

@app.exception_handler(StarletteHTTPException)
async def redirect_404_to_docs(request, exc):
    if exc.status_code == 404:
        return RedirectResponse(url="/docs")
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)
