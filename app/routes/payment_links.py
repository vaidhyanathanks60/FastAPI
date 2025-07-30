from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter()


class PaymentLinksListResponse(BaseModel):
    message: str

class PaymentLinkCreateRequest(BaseModel):
    amount: float

class PaymentLinkCreateResponse(BaseModel):
    link: str
    amount: float


@router.get("/", response_model=PaymentLinksListResponse)
def list_payment_links():
    return {"message": "Payment links working!"}

@router.post("/", response_model=PaymentLinkCreateResponse)
def create_payment_link(data: PaymentLinkCreateRequest):
    token = str(uuid.uuid4())[:8]
    return {"link": f"https://example.com/pay/{token}", "amount": data.amount}
