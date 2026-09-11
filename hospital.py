from Department import Department

class Hospital:
    
    def __init__(self, hospital_name: str, location: str)-> None:
        self.hospital_name = hospital_name
        self.location = location
        self.Department_list: list[Department] = []

    def add_department(self, department: Department)-> None:
        self.Department_list.append(department)
    
    def to_dict(self) -> dict:
        return {
            "hospital_name": self.hospital_name,
            "location": self.location,
            "Department_list": [department.to_dict() for department in self.Department_list]
        }