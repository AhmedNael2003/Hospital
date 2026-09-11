from person import Person

class Patient(Person):
    def __init__(self, name: str, age: int, medical_record: str) -> None:
        super().__init__(name, age)
        self.medical_record = medical_record
    def view_record(self) -> str:
        return f"{super().view_info()}, Medical Record: {self.medical_record}"
