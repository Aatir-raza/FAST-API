from pydantic import BaseModel, Field, computed_field
from typing import List, Dict

from field_validator import insert_user

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_detail: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi_value = round(self.weight / (self.height ** 2),2)
        return bmi_value
    

def update_patients_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.height)
    print('BMI:', patient.bmi)
    

patient_info ={'name':'raza','email':'raza@yahoo.com','age':'61','weight':70.5,'married':False,'height':1.75,'allergies':['pollen','dust'],'contact_detail':{'phone':'74374743', 'emergency_contact':'1234567890'}}

update_patients_data(patient=Patient(**patient_info))