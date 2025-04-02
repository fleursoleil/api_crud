# FastAPI CRUD with PostgreSQL

This project is a simple FastAPI application that demonstrates how to create a RESTful API that interacts with a PostgreSQL database. It supports CRUD (Create, Read, Update, Delete) operations on a `products` table.

### Features:
- Create new products in the database.
- Retrieve a list of all products.
- Retrieve a specific product by its ID.
- Update a product's details.
- Delete a product.

### Technologies Used:
- FastAPI: A modern Python web framework for building APIs.
- PostgreSQL: A powerful, open-source relational database.
- asyncpg: An asynchronous PostgreSQL database driver.
- Pydantic: Data validation and settings management for Python.

---

## Project Setup

### Prerequisites:
- Python 3.7 or higher
- PostgreSQL server running locally (or a remote server)
- `pip` for installing dependencies

### Installation:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fastapi-postgresql.git
    cd fastapi-postgresql
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      .\.venv\Scripts\activate
      ```
    - On Mac/Linux:
      ```bash
      source .venv/bin/activate
      ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup:

1. Ensure you have PostgreSQL installed and running.

2. Create a database `TestingLang` (or adjust the database name in the connection string if necessary).

3. Create the `products` table in PostgreSQL:
    ```sql
    CREATE TABLE products (
        productid SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        price FLOAT NOT NULL,
        tax FLOAT
    );
    ```

---

## Running the Application

1. Run the FastAPI application:
    ```bash
    uvicorn app:app --reload --host 0.0.0.0 --port 8000
    ```

    This will start the server on `http://127.0.0.1:8000`.

2. Open your browser and go to the following URL to interact with the API:
    - API Documentation (Interactive): `http://127.0.0.1:8000/docs`
    - OpenAPI schema: `http://127.0.0.1:8000/openapi.json`

---

## Endpoints

### 1. **Create a Product**
- **URL:** `/items/`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "Product Name",
        "description": "Product description",
        "price": 100.0,
        "tax": 10.0
    }
    ```

### 2. **Get All Products**
- **URL:** `/items/`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "productid": 1,
            "name": "Product Name",
            "description": "Product description",
            "price": 100.0,
            "tax": 10.0
        }
    ]
    ```

### 3. **Get a Product by ID**
- **URL:** `/items/{productid}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "productid": 1,
        "name": "Product Name",
        "description": "Product description",
        "price": 100.0,
        "tax": 10.0
    }
    ```

### 4. **Update a Product**
- **URL:** `/items/{productid}`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
        "name": "Updated Product Name",
        "description": "Updated description",
        "price": 120.0,
        "tax": 15.0
    }
    ```

### 5. **Delete a Product**
- **URL:** `/items/{productid}`
- **Method:** `DELETE`

---
