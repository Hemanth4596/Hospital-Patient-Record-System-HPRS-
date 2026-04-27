from datetime import datetime

class Ward:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []

    def assign_patient(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            patient.ward = self.name
            patient.admit_date = datetime.now()
            return True
        return False