import pytest
from src.keyboard import Keyboard

@pytest.fixture
def keyboard_fixture():
    """
    Фикстура для тестов Keyboard
    """
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard(keyboard_fixture):
    assert str(keyboard_fixture) == "Dark Project KD87A"
    assert str(keyboard_fixture.language) == "EN"
    keyboard_fixture.change_lang()
    assert str(keyboard_fixture.language) == "RU"

    # Сделали RU -> EN -> RU
    keyboard_fixture.change_lang().change_lang()
    assert str(keyboard_fixture.language) == "RU"

    keyboard_fixture.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter



