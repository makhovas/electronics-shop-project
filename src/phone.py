from src.item import Item


class Phone(Item):
    """Класс, который содержит все атрибуты класса Item и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
    """

    def __init__(self, __name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляров класса
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(__name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone{self.name, self.price, self.quantity, self.number_of_sim}"

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __add__(self, other):
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity

    def __radd__(self, other):
        """ Обратное сложение, не зависимо от порядка
        """
        return self.__add__(other)
