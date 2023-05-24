import pytest

from src.item import Item
from src.phone import Phone


def test_phone_add():
    dev1 = Item("Aple", 10000, 5)
    dev2 = Phone("Nokia", 80000, 3, 6)
    assert dev2 + dev1 == 8
    assert type(dev2 + dev1) is int
    