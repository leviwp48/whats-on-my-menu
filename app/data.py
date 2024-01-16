from models import FoodItem, User, Menu  # Import the FoodItem model
from typing import List, Dict
from pydantic import ValidationError


# USERS

def create_user(name: str, email: str, password: str) -> str:

    user_details = {
        "name": name.capitalize(),
        "email": email,
        "password": password
    }

    try:
        user = User(**user_details)
    except ValidationError as e:
        raise ValueError(f"Invalid user data: {e}")    

    # db call to save the user 
    return f"The user: {user}, was successfully created"


# FOOD ITEMS

def create_food_item(user_id: str, name: str, image_url: str, ingredients: List[str], notes: str, food_list: List[str]) -> str: #food_list is an example until I have a DB 

    print('here2')
    print(image_url)
    food_item_details = {
        "user_id": user_id,
        "name": name.capitalize(),
        "image_url": image_url,
        "ingredients": ingredients,
        "notes": notes
    }

    print(food_item_details)
    try:
        food_item = FoodItem(**food_item_details)
    except ValidationError as e:
        raise ValueError(f"Invalid user data: {e}")   

    # db call to save the food_item
    food_list.append(food_item)
    return f"The food_item: {food_item}, was successfully created"


def get_food_items(user_id: str, food_list: List[str]) -> List[str]: #food_list is an example until I have a DB 
    return food_list
    




# MENUS

def create_menu(user_id: str, name: str, meals: Dict, notes: str) -> str:

    menu_details = {
        "user_id": user_id,
        "name": name.capitalize(),
        "meals": meals,
        "notes": notes
    }

    try:
        menu = FoodItem(**menu_details)
    except ValidationError as e:
        raise ValueError(f"Invalid user data: {e}")   

    # db call to save the food_item
     
    return f"The menu: {menu}, was successfully created"