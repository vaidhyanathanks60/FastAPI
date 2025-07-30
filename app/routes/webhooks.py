from fastapi import APIRouter

router = APIRouter()

@router.post("/callback")
def callback(data: dict):
    # Simulate webhook callback
    print("Webhook received:", data)
    return {"message": "Webhook received"}