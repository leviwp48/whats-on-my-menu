from models import FoodItem
from typing import Dict
from pydantic import ValidationError


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