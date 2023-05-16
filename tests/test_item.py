"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("test_item", 10.0, 5)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0

def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0

def test_all_items():
    item1 = Item("item1", 5.0, 10)
    item2 = Item("item2", 7.0, 8)
    assert len(Item.all) == 2
    assert Item.all[0].name == "item1"
    assert Item.all[1].name == "item2"
