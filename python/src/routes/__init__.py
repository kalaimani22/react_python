from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import create_item, read_item, update_item, delete_item, read_all_items, get_db

router = APIRouter()

@router.post("/items/")
def create_item_route(name: str, description: str, db: Session = Depends(get_db)):
    return create_item({"name": name, "description": description})

@router.get("/items/{item_id}")
def read_item_route(item_id: int, db: Session = Depends(get_db)):
    item = read_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/")
def get_all_items(db: Session = Depends(get_db)):
    items = read_all_items(db)
    return items

@router.put("/items/{item_id}")
def update_item_route(item_id: int, name: str, description: str, db: Session = Depends(get_db)):
    return update_item(item_id, {"name": name, "description": description})

@router.delete("/items/{item_id}")
def delete_item_route(item_id: int, db: Session = Depends(get_db)):
    return delete_item(item_id)