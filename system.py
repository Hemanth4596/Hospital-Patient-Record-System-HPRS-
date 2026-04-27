from patient import Patient
from ward import Ward
from analytics import show_analytics
from datetime import datetime

class HPRS:
    def __init__(self):
        self.patients = {}
        self.wards = {
            "General": Ward("General", 5),
            "ICU": Ward("ICU", 2),
            "Private": Ward("Private", 3)
        }

    def add_patient(self):
        pid = input("Enter ID: ")

        if pid in self.patients:
            print("Patient already exists!")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")

        self.patients[pid] = Patient(pid, name, age, gender)
        print("Patient Registered!")

    def admit_patient(self):
        pid = input("Enter Patient ID: ")

        if pid not in self.patients:
            print("Patient not found!")
            return

        ward_name = input("Enter Ward (General/ICU/Private): ")

        if self.wards[ward_name].assign_patient(self.patients[pid]):
            print("Patient admitted!")
        else:
            print("Ward Full!")

    def billing(self):
        pid = input("Enter Patient ID: ")

        if pid in self.patients:
            total = 500 + 300 + 700
            self.patients[pid].bill += total
            print("Bill:", total)

    def search(self):
        pid = input("Enter Patient ID: ")

        if pid in self.patients:
            self.patients[pid].display()
        else:
            print("Not Found")

    def analytics(self):
        show_analytics(self.wards, self.patients)