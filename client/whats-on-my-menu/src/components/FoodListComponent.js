// src/components/FoodListComponent.js
import React from 'react';

const FoodListComponent = ({ foodItems, handleFoodClick }) => {
  return (
    <div className="food-list">
      <h2>Available Food Items</h2>
      <ul>
        {foodItems.map((food, index) => (
          <li key={index} onClick={() => handleFoodClick(food)}>
            {food.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FoodListComponent;
