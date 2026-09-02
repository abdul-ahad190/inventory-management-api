# Inventory Management API

A secure Inventory Management REST API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **JWT authentication**. The API provides full CRUD operations for products, categories, suppliers, and users, with protected routes and token-based authentication.

## Features

- 🔐 JWT-based authentication and protected routes
- 📦 Product management (CRUD)
- 🗂️ Category management (CRUD)
- 🏭 Supplier management (CRUD)
- 👤 User management and authentication
- 🗄️ PostgreSQL database with SQLAlchemy ORM
- 🔄 Database migrations with Alembic
- ✅ API tested with Postman

## Tech Stack

| Component        | Technology       |
|-------------------|------------------|
| Framework         | FastAPI          |
| Database          | PostgreSQL       |
| ORM               | SQLAlchemy       |
| Migrations        | Alembic          |
| Authentication    | JWT              |
| Testing           | Postman          |

## Project Structure

```
inventory-management-api/
├── alembic/              # Database migration scripts
├── src/
│   ├── products/         # Product module (model, schema, controller, router)
│   ├── categories/       # Category module
│   ├── suppliers/        # Supplier module
│   └── users/            # User module (auth included)
├── alembic.ini            # Alembic configuration
├── db.py                  # Database connection setup
├── main.py                 # Application entry point
├── pyproject.toml          # Project metadata and dependencies
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not committed)
```

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL installed and running

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abdul-ahad190/inventory-management-api.git
   cd inventory-management-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root with your database and JWT settings, for example:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/inventory_db
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## API Overview

| Resource    | Endpoints                                      |
|-------------|--------------------------------------------------|
| Users       | Register, login, get current user                |
| Products    | Create, read, update, delete products             |
| Categories  | Create, read, update, delete categories           |
| Suppliers   | Create, read, update, delete suppliers            |

> Full interactive documentation is available via Swagger UI at `/docs` once the server is running.

## Testing

API endpoints were tested using **Postman**. Import the collection (if included) or manually test endpoints using the Swagger UI at `/docs`.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with your proposed changes.

## License

This project currently has no license specified.
