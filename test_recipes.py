import pytest
from main import Ingredient, Recipe, ShoppingList

# Тестирование класса Ingredient
def test_ingredient_init():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"

def test_ingredient_str():
    ing = Ingredient("Мука", 500.0, "г")
    assert str(ing) == "Мука: 500.0 г"

def test_ingredient_eq():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 200.0, "г")
    ing3 = Ingredient("Сахар", 500.0, "г")
    ing4 = Ingredient("Мука", 500.0, "кг")
    
    assert ing1 == ing2
    assert ing1 != ing3
    assert ing1 != ing4
# Тестирование класса Recipe

def test_recipe_init():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    assert rec.title == "Пицца"
    assert rec.ingredients == [ing]

def test_recipe_add_ingredient_new():
    rec = Recipe("Пицца", [])
    ing = Ingredient("Мука", 500.0, "г")
    rec.add_ingredient(ing)
    assert len(rec.ingredients) == 1
    assert rec.ingredients[0].quantity == 500.0

def test_recipe_add_ingredient_existing():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 200.0, "г")
    rec = Recipe("Пицца", [ing1])
    rec.add_ingredient(ing2)
    assert len(rec.ingredients) == 1
    assert rec.ingredients[0].quantity == 700.0

def test_recipe_scale():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    
    scaled_rec = rec.scale(2.0)
    
    assert scaled_rec is not rec
    assert rec.ingredients[0].quantity == 500.0
    assert scaled_rec.ingredients[0].quantity == 1000.0

def test_recipe_scale_value_error():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    
    with pytest.raises(ValueError):
        rec.scale(-1)
        
    with pytest.raises(ValueError):
        rec.scale(0)

def test_recipe_len():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Сахар", 200.0, "г")
    rec = Recipe("Пицца", [ing1, ing2])
    assert len(rec) == 2

# Тестирование класса ShoppingList

def test_shopping_list_add_recipe():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    sl = ShoppingList()
    
    sl.add_recipe(rec, 2.0)
    assert len(sl._items) == 1
    assert sl._items[0][0].quantity == 1000.0

def test_shopping_list_add_recipe_value_error():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    sl = ShoppingList()
    
    with pytest.raises(ValueError):
        sl.add_recipe(rec, -1)
        
    with pytest.raises(ValueError):
        sl.add_recipe(rec, 0)

def test_shopping_list_remove_recipe():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    sl = ShoppingList()
    
    sl.add_recipe(rec, 1.0)
    sl.remove_recipe("Пицца")
    assert len(sl._items) == 0

def test_shopping_list_remove_recipe_not_found():
    ing = Ingredient("Мука", 500.0, "г")
    rec = Recipe("Пицца", [ing])
    sl = ShoppingList()
    
    sl.add_recipe(rec, 1.0)
    sl.remove_recipe("Суп")
    assert len(sl._items) == 1

def test_shopping_list_get_list():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Мука", 300.0, "г")
    ing3 = Ingredient("Апельсин", 2.0, "шт")
    
    rec1 = Recipe("Пицца", [ing1])
    rec2 = Recipe("Пирог", [ing2, ing3])
    
    sl = ShoppingList()
    sl.add_recipe(rec1, 1.0)
    sl.add_recipe(rec2, 1.0)
    
    result = sl.get_list()
    
    assert len(result) == 2
    assert result[0].name == "Апельсин"
    assert result[0].quantity == 2.0
    assert result[1].name == "Мука"
    assert result[1].quantity == 800.0

def test_shopping_list_add():
    ing1 = Ingredient("Мука", 500.0, "г")
    ing2 = Ingredient("Сахар", 200.0, "г")
    
    rec1 = Recipe("Пицца", [ing1])
    rec2 = Recipe("Торт", [ing2])
    
    sl1 = ShoppingList()
    sl1.add_recipe(rec1, 1.0)
    
    sl2 = ShoppingList()
    sl2.add_recipe(rec2, 1.0)
    
    combined = sl1 + sl2
    
    assert len(combined._items) == 2
    assert len(sl1._items) == 1
    assert len(sl2._items) == 1