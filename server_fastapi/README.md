# Event Horizon FastAPI Server

This is a FastAPI conversion of the original Express.js server from the Event Horizon project.

## Installation

1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection URI
   ```

## Running the Server

Start the FastAPI development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
server_fastapi/
├── main.py              # FastAPI application entry point
├── database.py          # MongoDB connection and utilities
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── models/
│   └── schemas.py       # Pydantic models for request/response validation
├── routers/
│   ├── event.py         # Event related endpoints
│   ├── station.py       # Station related endpoints
│   └── trajectory.py    # Trajectory related endpoints
└── controllers/
    ├── events.py        # Event business logic
    ├── station.py       # Station business logic
    └── trajectory.py    # Trajectory business logic
```

## API Endpoints

### Event Endpoints
- **GET /event/** - Search events
  - Query Parameters:
    - `searchQuery` (optional): Filter by shower code or region
    - `start` (optional): Start date (ISO format)
    - `end` (optional): End date (ISO format)

### Station Endpoints
- **GET /station/recorded** - Get station data
  - Query Parameters:
    - `station_name` (required): Station name

### Trajectory Endpoints
- **GET /trajectory/trajectory** - Get meteor trajectory data
  - Query Parameters:
    - `event_id` (required): Event ID

## Differences from Express Version

1. **Async/Await**: FastAPI uses async operations for better performance
2. **Motor**: Uses Motor async driver for MongoDB instead of Mongoose
3. **Pydantic**: Data validation through Pydantic models instead of Mongoose schemas
4. **CORS**: CORS middleware configured in main.py
5. **Auto Documentation**: Swagger UI automatically generated from FastAPI

## Environment Variables

- `MONGODB_URI`: MongoDB connection string (default: `mongodb://localhost:27017`)

## Notes

- The server uses Motor for asynchronous MongoDB operations
- CORS is configured to allow all origins (can be restricted in production)
- Error handling is implemented with proper HTTP status codes
- Database connection is managed through lifecycle events (startup/shutdown)
