from pydantic import BaseModel, EmailStr,Field,field_validator
from typing import List, Dict, Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight:float
    married: bool
    allergies: List[str]
    contact_detail:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'yahoo.com', 'outlook.com']
        # abc@gmail.com
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f'not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age must be between 0 and 100')


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