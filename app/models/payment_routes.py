from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.order import Order
from app.models.order_item import OrderItem
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/payment", tags=["Payment"])

class CartItem(BaseModel):
    id: int
    quantity: int
    price: float

class PaymentRequest(BaseModel):
    address: str
    phone: str
    total: float
    payment_method: str
    card_number: str
    expiry: str
    cvv: str
    items: List[CartItem]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/checkout")
def checkout(data: PaymentRequest, db: Session = Depends(get_db)):

    # 🔐 Validation simple
    if len(data.card_number) < 13 or len(data.cvv) < 3:
        raise HTTPException(status_code=400, detail="Informations bancaires invalides")

    new_order = Order(
        total=data.total,
        status="paid"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in data.items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(order_item)

    db.commit()

    return {
        "message": f"Paiement {data.payment_method} validé avec succès 🎉",
        "order_id": new_order.id
    }