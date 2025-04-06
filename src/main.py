from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import model, schema  # Use relative imports
from .database import SessionLocal, engine, Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory API v1")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Inventory API",
        "docs_url": "/docs",
        "available_endpoints": [
            "/products",
            "/products/{product_id}",
            "/products/{product_id}/stock-in",
            "/products/{product_id}/sale",
            "/products/{product_id}/manual-removal",
            "/products/{product_id}/movements",
            "/products/{product_id}/quantity"
        ]
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Products
@app.post("/products", response_model=schema.ProductOut)
def create_product(product: schema.ProductCreate, db: Session = Depends(get_db)):
    db_product = model.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products", response_model=list[schema.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(model.Product).all()

@app.get("/products/{product_id}", response_model=schema.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Stock Movements
def add_movement(product_id: int, movement_type: str, quantity: int, note: str, db: Session):
    product = db.query(model.Product).filter_by(id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    movement = model.StockMovement(
        product_id=product_id, type=movement_type,
        quantity=quantity, note=note
    )
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement

@app.post("/products/{product_id}/stock-in", response_model=schema.MovementOut)
def stock_in(product_id: int, data: schema.StockIn, db: Session = Depends(get_db)):
    return add_movement(product_id, "stock_in", data.quantity, data.note, db)

@app.post("/products/{product_id}/sale", response_model=schema.MovementOut)
def sell(product_id: int, data: schema.Sale, db: Session = Depends(get_db)):
    return add_movement(product_id, "sale", data.quantity, data.note, db)

@app.post("/products/{product_id}/manual-removal", response_model=schema.MovementOut)
def remove(product_id: int, data: schema.ManualRemoval, db: Session = Depends(get_db)):
    return add_movement(product_id, "manual_removal", data.quantity, data.note, db)

@app.get("/products/{product_id}/movements", response_model=list[schema.MovementOut])
def get_movements(product_id: int, db: Session = Depends(get_db)):
    return db.query(model.StockMovement).filter_by(product_id=product_id).all()

@app.get("/products/{product_id}/quantity")
def get_current_quantity(product_id: int, db: Session = Depends(get_db)):
    q = db.query(model.StockMovement).filter_by(product_id=product_id).all()
    total = 0
    for m in q:
        if m.type == "stock_in":
            total += m.quantity
        elif m.type in ["sale", "manual_removal"]:
            total -= m.quantity
    return {"product_id": product_id, "current_quantity": total}
