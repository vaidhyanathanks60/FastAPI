# payment_gateway/app/main.py
from fastapi import FastAPI
from app.routes import auth, payments, webhooks, payment_links

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["Webhooks"])
app.include_router(payment_links.router, prefix="/payment_links", tags=["Payment Links"])

@app.get("/")
def root():
    return {"message": "Welcome to Razorpay Clone API"}