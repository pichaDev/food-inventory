# Foodery 🍏

Food inventory management app built with FastAPI + PostgreSQL.

## Requirements

- Python 3.13+
- Docker & Docker Compose
- Git

## Setup

### 1. Clone

```bash
git clone <repository-url>
cd food-inventory
```

### 2. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 3. Database

PostgreSQL runs in a Docker container.

```bash
docker compose up -d
docker ps                   # verify it's running
alembic upgrade head
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

- API: <http://127.0.0.1:8000>
- Swagger docs: <http://127.0.0.1:8000/docs>

## Project Structure

```
food-inventory/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Config (Uvicorn, envs)
│   │   ├── db/           # Models & sessions
│   │   ├── schemas/      # Pydantic schemas
│   │   └── services/     # Business logic
│   ├── alembic/          # Migrations
│   └── requirements.txt
├── docker/
├── docs/
└── frontend/
```

## API Endpoints

| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| GET    | `/food-items`        | List all food items          |
| GET    | `/food-items/{id}`   | Get a food item by ID        |
| POST   | `/food-items`        | Create a new food item       |
| PUT    | `/food-items/{id}`   | Update an existing food item |
| DELETE | `/food-items/{id}`   | Delete a food item           |
