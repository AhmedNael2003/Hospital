from person import Person
class Staff(Person):
    def __init__(self, name: str, age: int, position: str) -> None:
        super().__init__(name, age)
        self.position = position

    def view_info(self) -> str:
        return f"{super().view_info()}, Position: {self.position}"