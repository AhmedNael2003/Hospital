
from Staff import Staff
from Patient import Patient
class Department:

    
   
    def __init__(self, department_name: str)-> None:
        self.department_name = department_name
        self.Patient_list: list[Patient] = []
        self.Staff_list: list[Staff] = []
    def add_patient(self, patient: Patient)-> None:
        self.Patient_list.append(patient)

    def to_dict(self) -> dict:
        return {
            "department_name": self.department_name,
            "Patient_list": [patient.view_record() for patient in self.Patient_list],
            "Staff_list": [staff.view_info() for staff in self.Staff_list]
        }

    def add_staff(self, staff: Staff)-> None:
        self.Staff_list.append(staff)