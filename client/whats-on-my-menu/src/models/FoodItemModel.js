// FoodItemModel.js
class FoodItemModel {
    constructor(data) {
      this.name = data.name;
      this.image_url = data.image_url;
      this.ingredients = data.ingredients;
      this.notes = data.notes;
    }
  
    printFoodName() {
      console.log(`Food Name: ${this.name}`);
    }
  }
  
  export default FoodItemModel;
  