from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncpg
from typing import List, Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


async def get_db_connection():
    conn = await asyncpg.connect(user="postgres", port=5432, password="passwordkosapostgresql", database="TestingLang", host="localhost")
    return conn


async def insert_data(name, description, price, tax):
    conn = await get_db_connection()
    query = """
        INSERT INTO products (name, description, price, tax) 
        VALUES ($1, $2, $3, $4)
        RETURNING productid;
    """
    productid = await conn.fetchval(query, name, description, price, tax)
    await conn.close()
    return productid


async def get_item(item_id: int):
    conn = await get_db_connection()
    query = "SELECT * FROM products WHERE productid = $1"
    row = await conn.fetchrow(query, item_id)
    await conn.close()
    return row


async def get_items():
    conn = await get_db_connection()
    query = "SELECT * FROM products"
    rows = await conn.fetch(query)
    await conn.close()
    return rows


async def update_item(item_id: int, name: str, description: Optional[str], price: float, tax: Optional[float]):
    conn = await get_db_connection()
    query = """
        UPDATE products
        SET name = $2, description = $3, price = $4, tax = $5
        WHERE productid = $1
        RETURNING *;
    """
    updated_item = await conn.fetchrow(query, item_id, name, description, price, tax)
    await conn.close()
    return updated_item


async def delete_item(item_id: int):
    conn = await get_db_connection()
    query = "DELETE FROM products WHERE productid = $1 RETURNING *;"
    deleted_item = await conn.fetchrow(query, item_id)
    await conn.close()
    return deleted_item


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    productid = await insert_data(item.name, item.description, item.price, item.tax)
    item_data = item.dict()
    item_data["productid"] = productid
    return item_data


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    item = await get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.get("/items/", response_model=List[Item])
async def read_items():
    items = await get_items()
    return items


@app.put("/items/{item_id}", response_model=Item)
async def update_item_endpoint(item_id: int, item: Item):
    updated_item = await update_item(item_id, item.name, item.description, item.price, item.tax)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@app.delete("/items/{item_id}", response_model=Item)
async def delete_item_endpoint(item_id: int):
    deleted_item = await delete_item(item_id)
    if deleted_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted_item

