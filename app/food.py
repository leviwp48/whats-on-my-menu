from models import FoodItem
from typing import List
from pydantic import ValidationError

# FOOD ITEMS

def create_food_item(user_id: str, name: str, image_url: str, ingredients: List[str], notes: str, food_list: List[str]) -> str: #food_list is an example until I have a DB 
    food_item_details = {
        "user_id": user_id,
        "name": name.capitalize(),
        "image_url": image_url,
        "ingredients": ingredients,
        "notes": notes
    }
    try:
        food_item = FoodItem(**food_item_details)
    except ValidationError as e:
        raise ValueError(f"Invalid user data: {e}")   

    # db call to save the food_item
    food_list[str(user_id)] = (food_item)
    return f"The food_item: {food_item}, was successfully created"


def get_food_items(user_id: str, food_list: List[str]) -> List[str]: #food_list is an example until I have a DB 
    return f"The food list for user: {user_id} is as follows: {food_list[user_id]}"


def get_food_item(user_id: str, food_name, food_list: List[str]) -> List[str]: #food_list is an example until I have a DB 
    return f"The food list for user: {user_id} is as follows: {food_list[food_name]}"