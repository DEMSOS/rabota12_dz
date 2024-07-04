class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def set_data(self, model, year, manufacturer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def get_data(self):
        return {
            'Модель': self.__model,
            'Год': self.__year,
            'Мануфактур': self.__manufacturer,
            'Громкость_двигателя': self.__engine_volume,
            'Цвет': self.__color,
            'Цена': self.__price
        }

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

# Пример использования
car = Car("Модель S", 2020, "Тесла", 2.0, "Красный", 50000)
print(car.get_data())
