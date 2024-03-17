import requests

# Assuming your FastAPI server is running on http://localhost:8000
base_url = "http://localhost:80"

# Data for creating a new food item
new_food_item_data = {
  "user_id": "asdlkjfs",
  "name": "Burger",
  "image_url": "https://example.com/burger.jpg",
  "ingredients": ["Ingredient1", "Ingredient2"],
  "notes": "Some notes about the food"
}

# Send a POST request to create a new food item
# response = requests.post(f"{base_url}/foods", json=new_food_item_data)

response = requests.get(f"{base_url}/foods")
print(response)
# Check the response
if response.status_code == 200:
    print("Food item created successfully")
else:
    print(f"Failed to create food item. Status code: {response.status_code}")
    print(response.json())  # Print the error details if available


foods = requests.get(f"{base_url}/foods")

print("here are the current foods: ", foods.json())