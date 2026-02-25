from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.restaurant import Restaurant
from app.schemas.restaurant_schema import RestaurantResponse
from typing import List

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()