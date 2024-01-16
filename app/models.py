# models.py
from typing import List
import uuid
from typing import Union, Dict
from pydantic import BaseModel, EmailStr


class FoodItem(BaseModel):
    id: str = str(uuid.uuid4())
    user_id: str
    name: str
    image_url: str
    ingredients: List[str]
    notes: Union[str, None] = None


class Menu(BaseModel):
    id: str = str(uuid.uuid4())
    user_id: str
    name: str
    meals: Dict[str, FoodItem]
    notes: Union[str, None] = None


class User(BaseModel):
    id: str = str(uuid.uuid4())
    name: str
    email: EmailStr
    hashed_password: str
    food_list: Union[List[FoodItem], None] = None
    menu: Union[Menu, None] = None
