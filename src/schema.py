from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class MovementBase(BaseModel):
    quantity: int
    note: Optional[str] = None

class StockIn(MovementBase):
    pass

class Sale(MovementBase):
    pass

class ManualRemoval(MovementBase):
    pass

class MovementOut(BaseModel):
    id: int
    type: str
    quantity: int
    timestamp: datetime
    note: Optional[str]
    class Config:
        from_attributes = True
