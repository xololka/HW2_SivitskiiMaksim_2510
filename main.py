class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, val):
        f_val = float(val)
        if f_val <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = f_val

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit

class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for existing_ing in self.ingredients:
            if existing_ing == ingredient:
                existing_ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) in (int, float):
            return ratio > 0
        return False

    def scale(self, ratio: float):
        new_ings = []
        for ing in self.ingredients:
            new_ing = Ingredient(ing.name, ing.quantity * ratio, ing.unit)
            new_ings.append(new_ing)
        return Recipe(self.title, new_ings)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        lines = [self.title]
        for ing in self.ingredients:
            lines.append(f"- {ing}")
        return "\n".join(lines)

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        sc_rec = recipe.scale(portions)
        for ing in sc_rec.ingredients:
            self._items.append((ing, recipe.title))

    def remove_recipe(self, title: str):
        new_items = []
        for ing, r_title in self._items:
            if r_title != title:
                new_items.append((ing, r_title))
        self._items = new_items

    def get_list(self):
        d = {}
        for ing, _ in self._items:
            k = (ing.name, ing.unit)
            if k in d:
                d[k] += ing.quantity
            else:
                d[k] = ing.quantity
        
        res = []
        for (n, u), q in d.items():
            res.append(Ingredient(n, q, u))
            
        res.sort(key=lambda x: x.name)
        return res

    def __add__(self, other):
        new_sl = ShoppingList()
        new_sl._items = self._items.copy() + other._items.copy()
        return new_sl

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list = None):
        if ingredients is None:
            ingredients = []
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        sc_rec = super().scale(ratio)
        return DietaryRecipe(sc_rec.title, self.diet_type, sc_rec.ingredients)

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"