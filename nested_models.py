from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin_code: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Ranchi', 'state': 'jharkhand', 'pin_code': '834001'}    

address1=Address(**address_dict)

patient_info = {'name': 'raza', 'gender': 'male', 'age': 20, 'address': address_dict}

patient1=Patient(**patient_info)

print(patient1)
print(patient1.address.city)
print(patient1.name)