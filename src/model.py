from sqlalchemy import Column, DateTime, ForeignKey , Integer , String   
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func 
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer , primary_key=True)
    name = Column(String , index=True)
    sku = Column(String , index=True, unique=True)
    description = Column(String , nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    movements = relationship("StockMovement", back_populates="product")




class StockMovement(Base):

    __tablename__ = "movements"
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))    
    type = Column(String) # stock_in, sale, manual_removal
    quantity = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    note = Column(String, nullable=True)
    product = relationship("Product", back_populates="movements")