from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base, SessionLocal

# Models
from app.models.user import User
from app.models.product import Product
from app.models.restaurant import Restaurant
from app.models.order import Order
from app.models.order_item import OrderItem

# Routes
from app.routes.user_routes import router as user_router
from app.routes.product_routes import router as product_router
from app.routes.restaurant_routes import router as restaurant_router
from app.routes.payment_routes import router as payment_router

app = FastAPI()
app.include_router(payment_router)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(restaurant_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Lunchify API is running 🚀"}


def seed_data():
    db = SessionLocal()

    if db.query(Restaurant).count() == 0:

        r1 = Restaurant(
            name="Pasta Express",
            description="Cuisine italienne maison.",
            image_url="https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=800&q=80"
        )

        r2 = Restaurant(
            name="Burger Lab",
            description="Burgers gourmets premium.",
            image_url="https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80"
        )

        r3 = Restaurant(
            name="Healthy Bowl",
            description="Plats healthy et frais.",
            image_url="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80"
        )

        db.add_all([r1, r2, r3])
        db.commit()

    if db.query(Product).count() == 0:

        pasta = db.query(Restaurant).filter_by(name="Pasta Express").first()
        burger = db.query(Restaurant).filter_by(name="Burger Lab").first()
        healthy = db.query(Restaurant).filter_by(name="Healthy Bowl").first()

        products = [

            # Pasta
            Product(name="Riz sauté aux crevettes",
                    description="Riz frit aux crevettes fraîches et légumes croquants.",
                    price=8.5,
                    image_url="https://images.unsplash.com/photo-1512058564366-c9e3e046a1c3?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=pasta.id),

            Product(name="Carbonara",
                    description="Pâtes crémeuses au parmesan.",
                    price=9.2,
                    image_url="https://images.unsplash.com/photo-1608756687911-aa1599ab3bd9?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=pasta.id),

            Product(name="Lasagnes",
                    description="Lasagnes maison au bœuf mijoté.",
                    price=10.5,
                    image_url="https://images.unsplash.com/photo-1619895092538-128341789043?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=pasta.id),

            Product(name="Pizza Margherita",
                    description="Tomate, mozzarella et basilic frais.",
                    price=11.0,
                    image_url="https://images.unsplash.com/photo-1548365328-8b849f3c8f76?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=pasta.id),

            Product(name="Gnocchis Pesto",
                    description="Gnocchis frais sauce pesto maison.",
                    price=10.0,
                    image_url="https://images.unsplash.com/photo-1598514982847-6a6e4a4a7b18?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=pasta.id),

            # Burger
            Product(name="Cheese Burger",
                    description="Steak grillé et cheddar fondant.",
                    price=9.9,
                    image_url="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=burger.id),

            Product(name="Double Bacon",
                    description="Double steak bacon croustillant.",
                    price=11.5,
                    image_url="https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=burger.id),

            Product(name="Chicken Burger",
                    description="Poulet crispy et sauce maison.",
                    price=9.0,
                    image_url="https://images.unsplash.com/photo-1606755962773-d324e0a13086?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=burger.id),

            Product(name="Wrap Poulet",
                    description="Wrap poulet grillé et crudités.",
                    price=8.9,
                    image_url="https://images.unsplash.com/photo-1606755456206-b25206bfa433?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=burger.id),

            Product(name="Tacos Mixte",
                    description="Poulet et viande hachée gratinée.",
                    price=9.5,
                    image_url="https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=burger.id),

            # Healthy
            Product(name="Healthy Bowl",
                    description="Quinoa, avocat et poulet grillé.",
                    price=7.9,
                    image_url="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=healthy.id),

            Product(name="Vegan Bowl",
                    description="Pois chiches et légumes grillés.",
                    price=7.5,
                    image_url="https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=healthy.id),

            Product(name="Green Smoothie",
                    description="Épinard, kiwi et banane.",
                    price=4.5,
                    image_url="https://images.unsplash.com/photo-1497534446932-c925b458314e?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=healthy.id),

            Product(name="Salade César",
                    description="Poulet grillé et parmesan.",
                    price=7.8,
                    image_url="https://images.unsplash.com/photo-1550304943-4f24f54ddde9?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=healthy.id),

            Product(name="Milkshake Chocolat",
                    description="Milkshake chocolat intense.",
                    price=5.5,
                    image_url="https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=800&q=80",
                    restaurant_id=healthy.id),
        ]

        db.add_all(products)
        db.commit()

    db.close()


seed_data()