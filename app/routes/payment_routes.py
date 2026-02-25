import stripe
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/payment", tags=["Payment"])

stripe.api_key = "TA_CLE_TEST_STRIPE_ICI"

class PaymentRequest(BaseModel):
    amount: int  # en centimes

@router.post("/create-payment-intent")
def create_payment_intent(data: PaymentRequest):
    intent = stripe.PaymentIntent.create(
        amount=data.amount,
        currency="eur",
        payment_method_types=["card"],
    )
    return {"clientSecret": intent.client_secret}