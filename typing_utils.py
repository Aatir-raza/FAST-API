from pydantic import BaseModel
from typing import List,Dict,optional

class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married: bool
    allergies: optional[List[str]] = None
    contact_detail:Dict[str,str]

def insert_user(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted')

patient_info ={'name':'raza','age':20,'weight':70.5,'married':False,'allergies':['pollen','dust'],'contact_detail':{'email':'abc@gmail.com','phone':'1234567890'}}

patient1=Patient(**patient_info)

insert_user(patient1)      