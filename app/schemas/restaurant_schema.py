from pydantic import BaseModel


class RestaurantResponse(BaseModel):
    id: int
    name: str
    description: str
    image_url: str

    class Config:
        from_attributes = True