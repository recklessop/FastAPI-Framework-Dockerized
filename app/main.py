from fastapi import FastAPI
import redis

app = FastAPI()

# Connect to Redis database
r = redis.Redis(host='redis', port=6379)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: dict):
    # Store the item in the Redis database
    r.set(item_id, item)
    return {"item_id": item_id, "item": item}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Retrieve the item from the Redis database
    item = r.get(item_id)
    if item:
        return {"item_id": item_id, "item": item}
    else:
        return {"error": "Item not found"}

