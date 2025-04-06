# Inventory Management API

This project is a simple Inventory Management API built using **FastAPI** and **SQLAlchemy**. It provides endpoints to manage products, track stock movements, and calculate current product quantities. The API is designed to be lightweight and easy to use, with SQLite as the default database.

## Features
- Add, list, and retrieve products.
- Record stock movements (stock-in, sales, manual removal).
- View stock movement history for a product.
- Calculate the current quantity of a product.

## Tech Stack
- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite**: Lightweight database for local storage.
- **Pydantic**: Data validation and serialization.
- **Uvicorn**: ASGI server for running the application.

## Prerequisites
- Python 3.10 or higher installed on your system.
- `pip` (Python package manager) installed.
- Optional: `virtualenv` for creating isolated environments.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
cd phase_1
```

### 2. Configure Environment Variables
- Copy the `.env.example` file to `.env`:
  ```bash
  cp .env.example .env
  ```
- The `.env` file contains the database URL. By default, it uses SQLite:
  ```
db_url = "sqlite:///inventory.db"
  ```

### 3. Create a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
The database tables are automatically created when the application starts. Ensure the database URL in `.env` is correct.

### 6. Start the Application
Run the application using the `run.py` script:
```bash
python run.py
```

The API will be available at `http://127.0.0.1:8000`.

### 7. Access the API Documentation
FastAPI provides interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure
```
phase_1/
├── .env.example          # Example environment variables
├── .env                  # Environment variables (ignored by Git)
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── run.py                # Entry point to run the application
├── src/
│   ├── database.py       # Database configuration
│   ├── main.py           # FastAPI application and routes
│   ├── model.py          # SQLAlchemy models
│   ├── schema.py         # Pydantic schemas
```

## Endpoints Overview
- **GET /**: Welcome message and available endpoints.
- **POST /products**: Create a new product.
- **GET /products**: List all products.
- **GET /products/{product_id}**: Retrieve a product by ID.
- **POST /products/{product_id}/stock-in**: Record stock-in movement.
- **POST /products/{product_id}/sale**: Record a sale movement.
- **POST /products/{product_id}/manual-removal**: Record manual stock removal.
- **GET /products/{product_id}/movements**: View stock movement history.
- **GET /products/{product_id}/quantity**: Get the current quantity of a product.

## Notes
- The database file (`inventory.db`) is automatically created in the project root.
- To reset the database, delete the `inventory.db` file and restart the application.

## License
This project is open-source and available under the MIT License.