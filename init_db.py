# payment_gateway/init_db.py
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.models.user import User
from app.models.payment import Payment
from app.utils.auth import hash_password

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    # Check if users already exist
    if db.query(User).count() > 0:
        print("DB already initialized.")
        return

    print("Inserting sample users...")

    user1 = User(
        email="merchant@example.com",
        hashed_password=hash_password("merchant123"),
        role="merchant"
    )
    user2 = User(
        email="user@example.com",
        hashed_password=hash_password("user123"),
        role="user"
    )

    db.add_all([user1, user2])
    db.commit()

    print("Creating sample payments...")

    payment1 = Payment(amount=500.0, status="success", user_id=1)
    payment2 = Payment(amount=250.0, status="pending", user_id=2)

    db.add_all([payment1, payment2])
    db.commit()

    print("Database initialized with sample data.")

if __name__ == "__main__":
    init_db()
