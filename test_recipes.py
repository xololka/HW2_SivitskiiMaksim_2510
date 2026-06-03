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
