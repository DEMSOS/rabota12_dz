class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def set_data(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def get_data(self):
        return {
            'Имя': self.__name,
            'Дата открытия': self.__opening_date,
            'Страна': self.__country,
            'Город': self.__city,
            'Доп_пункт': self.__capacity
        }

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

# Пример использования
stadium = Stadium("Национальный стадион", "2022-01-01", "Страна A", "Город B", 50000)
print(stadium.get_data())
