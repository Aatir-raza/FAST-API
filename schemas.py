from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_user(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

patient_info ={'name':'raza','age':20}

patient1=Patient(**patient_info)

insert_user(patient1)  