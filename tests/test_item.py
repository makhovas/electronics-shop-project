import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone

@pytest.fixture
def item_fixture():
    """
    Фикстура для тестов Item
    """
    return Item('Смартфон', 10000, 20)


def test_item_init(item_fixture):
    """
    Проверяем, что в есть такое название товара и длину названия
    """
    assert item_fixture.name == "Смартфон"
    assert len(item_fixture.name) <= 10


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


def test_string_to_number():
    """
    Проверяем, что строковые значения возвращаются числом независимо от типа
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    """
    Проверяем кол-во записей по товарам
    """
    assert len(Item.all) == 3


def test_repr(item_fixture):
    """Тест метода репр"""
    assert repr(item_fixture) == "Item('Смартфон', 10000, 20)"


def test_str(item_fixture):
    """Тест метода стр"""
    assert str(item_fixture) == 'Смартфон'

def test_add_and_radd_phone_and_item():
    """
    Тест методов add и radd для классов Item и Phone
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25

def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/items.csv')

def test_instantiate_from_csv_file_broken():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items_failed.csv")

