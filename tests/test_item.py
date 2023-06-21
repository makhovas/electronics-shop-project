import pytest
from src.item import Item

@pytest.fixture
def item_fixture():
    """
    Фикстура для тестов
    """
    return Item("Смартфон", 10000, 20)

def test_item_init(item_fixture):
    """
    Проверяем, что в есть такое название товара
    """
    assert item_fixture.name == "Смартфон"

def test_calculate_total_price(item_fixture):
    """
    Проверяем, что сумма товаров равна заданному числу
    """
    assert item_fixture.price * item_fixture.quantity == 200000

def test_apply_discount(item_fixture):
    """
    Проверяем, что цена со скидкой равна заданному числу
    """
    assert item_fixture.price * 0.8 == 8000.0
