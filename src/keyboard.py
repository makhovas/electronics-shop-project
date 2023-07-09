from src.item import Item


class MixinLanguage:
    """
    Миксин класс с методом для изменения языка (раскладки клавиатуры)
    """

    def __init__(self, language='EN'):
        self.language = language

    def change_lang(self):
        """
        Метод для изменения языка (раскладки клавиатуры)
        """
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        return self


class Keyboard(Item, MixinLanguage):
    """
    Класс, который содержит все атрибуты класса Item и дополнительно атрибут
    language и метод для изменения языка (раскладки клавиатуры).
    """

    def __init__(self, __name: str, price: float, quantity: int):
        """
        Создание экземпляров класса
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(__name, price, quantity)
        MixinLanguage.__init__(self)
