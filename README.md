# PokePipeline Backend

The backend service for the PokePipeline application, built with FastAPI and SQLAlchemy.

## 🛠️ Tech Stack

- FastAPI - Modern, fast web framework for building APIs
- SQLAlchemy - SQL toolkit and ORM
- PokeBase - Pokémon API wrapper
- SQLite - Lightweight database
- Pydantic - Data validation and settings management

## 📁 Project Structure

```
backend/
├── app/
│   ├── api/            # API routes
│   ├── db/             # Database configuration
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   └── main.py         # Application entry point
└── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r app/requirements.txt
```

3. Run the development server:
```bash
uvicorn app.main:app --reload
```

The server will start at `http://localhost:8000`

## 📝 API Endpoints

### GET /api/pokemon
Returns a list of all Pokémon in the database.

Response:
```json
[
  {
    "id": 1,
    "name": "bulbasaur",
    "height": 7,
    "weight": 69,
    "types": "grass, poison",
    "abilities": "overgrow, chlorophyll"
  }
]
```

## 🔧 Configuration

The application uses SQLite as its database. The database file is automatically created when the application starts.

## 📚 API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧪 Testing

To run tests:
```bash
pytest
```

## 📄 License

This project is licensed under the MIT License. 