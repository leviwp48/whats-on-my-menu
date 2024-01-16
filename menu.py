
class Menu:
    def __init__(self) -> None:
        self._menu = {
            "breakfast": [],
            "lunch": [],
            "dinner": []
        }
        # do I need this? 
        self._suggestions = {
            "breakfast": [],
            "lunch": [],
            "dinner": []
        }

    @property
    def menu(self):
        return self._menu
    
    
    @property
    def suggestions(self):
        return self._suggestions
    

    def add_food(self, food, time, category):
        if category == "menu":
            if time == "breakfast":
                self._menu[time].append(food)
            elif time == "lunch":
                self._menu[time].append(food)
            else:
                self._menu[time].append(food)
        elif category == "suggestions":
            if time == "breakfast":
                self._suggestions[time].append(food)
            elif time == "lunch":
                self._suggestions[time].append(food)
            else:
                self._suggestions[time].append(food)

    