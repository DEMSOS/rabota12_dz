class Parent:
    def __init__(self, text):
        self.text = text

    def show_text(self):
        print(self.text)

class Child(Parent):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def show_info(self):
        print(f"Текст: {self.text}, Номер: {self.number}")

# Пример использования
parent = Parent("Привет от родителя")
parent.show_text()

child = Child("Привет от ребёнка", 42)
child.show_info()
