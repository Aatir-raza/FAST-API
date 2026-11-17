from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional
import json

from post_operation import Patient, save_data

router = APIRouter()

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]
                                      
@router.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = data_load()


    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_patient = data[patient_id]
    

    # Update the patient data with the provided fields
    updated_patient_info = patient_update.model_dump(exclude_unset=True)


    for key, value in updated_patient_info.items():
        existing_patient[key] = value

    existing_patient['id'] = patient_id
    patient_pydantic = Patient(**existing_patient)
    data[patient_id] = patient_pydantic.model_dump(exclude={'id'})

    save_data(data)

    return JSONResponse(
        content={"message": "Patient updated successfully", "patient": data[patient_id]},
        status_code=200,
    )

def data_load():
    with open(r"C:\Users\Homes\Desktop\FASTAPI\patients.json", "r") as f:
        data = json.load(f)
    return data    
