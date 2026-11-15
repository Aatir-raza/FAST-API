from pydantic import BaseModel, EmailStr,model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float
    married: bool
    allergies: List[str]
    contact_detail:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency_contact' not in model.contact_detail:
            raise ValueError('Emergency contact is required for patients above 60 years old')
        return model

def insert_user(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_detail)
    print(patient.email)
    print(patient.married)
    print('updated')
    print('inserted')

patient_info ={'name':'raza','email':'raza@yahoo.com','age':'61','weight':70.5,'married':False,'allergies':['pollen','dust'],'contact_detail':{'phone':'74374743', 'emergency_contact':'1234567890'}}

patient1=Patient(**patient_info)

insert_user(patient1)  