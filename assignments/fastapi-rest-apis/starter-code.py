from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    name: str
    description: str
    price: float
    on_offer: bool

# Rotas CRUD
@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item criado com sucesso!", "item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"message": f"Detalhes do item {item_id}"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"message": f"Item {item_id} atualizado com sucesso!", "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} removido com sucesso!"}