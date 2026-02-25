from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str
    restaurant_id: int

    class Config:
        from_attributes = True