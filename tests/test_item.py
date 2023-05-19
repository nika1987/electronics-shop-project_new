"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("test_item", 10.0, 5)

@pytest.fixture
def items_csv():
    Item.instantiate_from_csv("src/items.csv")
    return Item.all


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0

def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0

def test_all_items():
    item1 = Item("item1", 5.0, 10)
    item2 = Item("item2", 7.0, 8)
    assert len(Item.all) == 4
    assert Item.all[2].name == "item1"
    assert Item.all[3].name == "item2"


def test_instantiate_from_csv(items_csv):
    assert len(items_csv) == 10
    assert isinstance(items_csv[0], Item)
    assert items_csv[0].name == "Смартфон"
    assert items_csv[0].price == 100
    assert items_csv[0].quantity == 1
    assert items_csv[2].name == "Ноутбук"
    assert items_csv[2].price == 1000
    assert items_csv[2].quantity == 3

def test_item_repr():
    item = Item("test item", 10.99, 5)
    assert repr(item) == "Item('test item', 10.99, 5)"

def test_item_str():
    item = Item("test item", 10.99, 5)
    assert str(item) == "test item"
