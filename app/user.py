from models import User  # Import the FoodItem model
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

