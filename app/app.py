# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import FoodItem, User, Menu  # Import the FoodItem model
from food import create_food_item, get_food_items, get_food_item
from menu import create_menu
from user import create_user


## GET request 
# curl "http://127.0.0.1:80"

## POST request 
# curl -X POST -H "Content-Type: application/json" -d '{
#   "id": "feef3964-f60d-40bf-89fc-5d5f2a23239b",
#   "user_id": "71a83264-435a-4c10-a967-405bc8d1a55a",
#   "name": "Spaghetti",
#   "image_url": "spaghetti2.jpeg",
#   "ingredients": ["pasta", "tomatoes"],
#   "notes": "this is my user hehe"
# }' http://127.0.0.1:80/foods
# {"message":"Food item created successfully"}

## the id might change ??? 
# curl "http://127.0.0.1:8000/foods?userId=71a83264-435a-4c10-a967-405bc8d1a55a"


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
foods_db = {}


@app.get("/")
async def root():
    x = {
        "name": "test_user".capitalize(),
        "email": "leviwp48@gmail.com",
        "hashed_password": "asldfjds",
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

    food_item = FoodItem(**y)

    updated_user = user.copy(update={"food_list": food_item})

    print(user)
    print(food_item)
    print(updated_user)
    return updated_user

# User

## Food

# create a food
@app.post("/foods")
async def create_food(food_item: FoodItem):
    create_food_item(food_item.user_id, food_item.name, food_item.image_url, food_item.ingredients, food_item.notes, foods_db)
    print('food list: ', foods_db)
    return {"message": "Food item created successfully"}

# get a list of all food items
@app.get("/foods")
async def retrieve_food_items(user_id: str):
    return get_food_items(user_id, foods_db)

# get a single food item by name 
@app.get("/foods/{food_id}")
async def retrieve_food_item(user_id: int, food_name: str):
    return get_food_item(user_id, food_name, foods_db)


# Menu