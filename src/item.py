import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, __name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all = self.all.append(self)

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        if not os.path.exists(path):
            raise FileNotFoundError('Отсутствует файл item.csv.')
        cls.all.clear()
        with open(path, 'r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if set(row) != {'name', 'price', 'quantity'}:
                    raise InstantiateCSVError()
                else:
                    cls(row['name'], cls.string_to_number(row['price']), cls.string_to_number(row['quantity']))

    @staticmethod
    def string_to_number(string):
        return int(float(string))


class InstantiateCSVError(Exception):
    """Класс для обработки исключений по файлу csv"""

    def __init__(self, message='Файл item.csv поврежден.'):
        super().__init__(message)

