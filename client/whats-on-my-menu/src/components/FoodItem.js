// src/components/Food.js
import React, { useState, useEffect } from 'react';
import FoodListComponent from './FoodListComponent';

function FoodItem() {
  const [foodItems, setFoodItems] = useState([]);
  const [selectedFood, setSelectedFood] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8001/foods')
      .then(response => response.json())
      .then(data => setFoodItems(data));
  }, []);

  const handleFoodClick = (food) => {
    setSelectedFood(food);
  };

  return (
    <div className="App">
      <FoodListComponent foodItems={foodItems} handleFoodClick={handleFoodClick} />
      <div className="main-list">
        {selectedFood ? (
          <>
            <h2>{selectedFood.name}</h2>
            <img src={selectedFood.image_url} alt={selectedFood.name} />
            <h3>Ingredients:</h3>
            <ul>
              {selectedFood.ingredients.map((ingredient, index) => (
                <li key={index}>{ingredient}</li>
              ))}
            </ul>
            <h3>Notes:</h3>
            <p>{selectedFood.notes}</p>
          </>
        ) : (
          <p>Select a food item to view details.</p>
        )}
      </div>
    </div>
  );
}

export default FoodItem;
