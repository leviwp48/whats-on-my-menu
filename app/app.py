# main.py
from fastapi import FastAPI, HTTPException
from typing import List
from models import FoodItem, User, Menu  # Import the FoodItem model
from fastapi.middleware.cors import CORSMiddleware
from data import create_food_item, get_food_items

app = FastAPI()

# Allow all origins during development. Adjust this in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data storage for demonstration purposes
foods_db = []



@app.get("/")
async def root():
    x = {
        "name": "test_user".capitalize(),
        "notes": "this is my user hehe"
    }
    user = User(**x)

    y = {
        "user_id": str(user.id),
        "name": "spaghetti".capitalize(),
        "image_url": "spagehtti2.jpeg",
        "ingredients": ["pasta", "tomatoes"],
        "notes": "this is my user hehe"
    }

    foodItem = FoodItem(**y)

    updated_user = user.copy(update={"food_list": foodItem})

    print(user)
    print(foodItem)
    print(updated_user)
    return updated_user


@app.post("/foods")
async def create_food(foodItem: FoodItem):
    print('hrereere')
    create_food_item(foodItem.user_id, foodItem.name, foodItem.image_url, foodItem.ingredients, foodItem.notes, foods_db)
    return {"message": "Food item created successfully"}


@app.get("/foods")
async def get_food_items():
    return get_food_items()


@app.get("/foods/{food_id}")
async def get_food_item(food_id: int):
    try:
        return foods_db[food_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Food item not found")

