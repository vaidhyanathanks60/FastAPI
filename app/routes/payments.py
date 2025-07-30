# payment_gateway/app/routes/payments.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.payment import Payment

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/initiate")
def initiate_payment(amount: float, user_id: int, db: Session = Depends(get_db)):
    payment = Payment(amount=amount, user_id=user_id)
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return {"payment_id": payment.id, "status": payment.status}

@router.get("/{payment_id}")
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(Payment).get(payment_id)
    return {"id": payment.id, "amount": payment.amount, "status": payment.status}