# Inventory Management API

A RESTful Inventory Management API built with Python and FastAPI.

The project provides user authentication and CRUD operations for products, categories, and suppliers using PostgreSQL and SQLAlchemy.

## 🚀 Features

- User registration
- User login
- JWT authentication
- Password hashing
- Protected API routes
- Product CRUD operations
- Category CRUD operations
- Supplier CRUD operations
- PostgreSQL database
- SQLAlchemy ORM
- Alembic database migrations
- Pydantic validation
- RESTful API architecture
- Postman API testing

## 🛠️ Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT
- Uvicorn
- Postman

## 📁 Project Structure

```text
inventory-management-api/
│
├── alembic/
│   └── versions/
│
├── src/
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   └── security.py
│   │
│   ├── categories/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── model.py
│   │   ├── router.py
│   │   └── schema.py
│   │
│   ├── products/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── model.py
│   │   ├── router.py
│   │   └── schema.py
│   │
│   ├── suppliers/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── model.py
│   │   ├── router.py
│   │   └── schema.py
│   │
│   └── users/
│       ├── __init__.py
│       ├── controller.py
│       ├── model.py
│       ├── router.py
│       └── schema.py
│
├── .gitignore
├── alembic.ini
├── db.py
├── main.py
├── pyproject.toml
└── README.md
