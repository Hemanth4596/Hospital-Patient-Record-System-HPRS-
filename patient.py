from datetime import datetime

class Patient:
    def __init__(self, pid, name, age, gender):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.ward = None
        self.admit_date = None
        self.discharge_date = None
        self.bill = 0

    def stay_duration(self):
        if self.admit_date and self.discharge_date:
            return (self.discharge_date - self.admit_date).days
        return 0

    def display(self):
        print(f"ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Ward: {self.ward}")
        print(f"Bill: ₹{self.bill}")