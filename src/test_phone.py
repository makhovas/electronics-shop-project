from src.phone import Phone
import pytest

@pytest.fixture
def phone_fixture():
    """
    Фикстура для тестов Phone
    """
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone_fixture):
    """
    Проверяем, что в есть такое название товара и кол-во сим-карт
    """
    assert phone_fixture.name == "iPhone 14"
    assert phone_fixture.number_of_sim == 2


def test_repr_phone(phone_fixture):
    """Тест метода репр класса Phone
    """
    assert repr(phone_fixture) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_phone(phone_fixture):
    """Тест метода стр класса Phone"""
    assert str(phone_fixture) == 'iPhone 14'

def test_add_and_radd_phone_and_item():
    """
    Тест методов add и radd для классa Phone
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1 + phone1 == 10