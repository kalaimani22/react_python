from sqlalchemy.orm import Session
from ..models import Item, SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_item(data):
    db = next(get_db())
    db_item = Item(name=data['name'], description=data['description'])
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_item(item_id):
    db = next(get_db())
    return db.query(Item).filter(Item.id == item_id).first()

def read_all_items(db: Session):
    return db.query(Item).all()

def update_item(item_id, data):
    db = next(get_db())
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db_item.name = data['name']
        db_item.description = data['description']
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(item_id):
    db = next(get_db())
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item