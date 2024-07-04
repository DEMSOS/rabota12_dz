class Book:
    def __init__(self, title, year, publisher, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__author = author
        self.__price = price

    def set_data(self, title, year, publisher, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__author = author
        self.__price = price

    def get_data(self):
        return {
            'Заголовок': self.__title,
            'Год': self.__year,
            'Публикация': self.__publisher,
            'Автор': self.__author,
            'Цена': self.__price
        }

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

# Пример использования
book = Book("Питон разработка", 2021, "Публикация XYZ", "Автор ABC", 45)
print(book.get_data())
