import pytest

from project import add_products, delete, update

def test_add_products():
    inventory = []
    add_products(inventory, "Remera", "Nike", 10, 1500.0)

    assert len(inventory) == 1
    assert inventory[0]["name"] == "Remera"
    assert inventory[0]["id"] == 1

def test_delete():
    inventory = []
    add_products(inventory, "Monitor", "HP", 1, 1000.0)

    inventory = delete(inventory, 1)

    assert len(inventory) == 0

def test_update():
    inventory = [{"id": 1, "name": "Remera", "brand": "Nike", "amount": 10, "price": 1500.0}]
    
    for p in inventory:
        if p["id"] == 1:
            p["name"] = "Pantalon"
            break
    
    assert inventory[0]["name"] == "Pantalon"

