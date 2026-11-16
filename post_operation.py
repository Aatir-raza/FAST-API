from fastapi import FastAPI, HTTPException, Query, Path,APIRouter
from fastapi.responses import JSONResponse
from typing import Annotated
from pydantic import BaseModel, Field,computed_field
import json

from patients import load_data

router = APIRouter()


class Patient(BaseModel):

    id: Annotated[str, Field(..., description="The ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="Name of the patient", example="John Doe")]
    city: Annotated[str, Field(..., description="City of the patient", example="New York")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient", example=30)]
    gender: Annotated[str, Field(..., description="Gender of the patient", example="Male")]
    height: Annotated[float, Field(..., description="Height of the patient in cm", example=175.5)]
    weight: Annotated[float, Field(..., description="Weight of the patient in kg", example=70.0)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight / ((self.height / 100) ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict (self) -> str:

        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 25:
            return 'normal'
        elif self.bmi <30:
            return 'normal'
        else:
            return 'obese'

def data_load():
    with open(r"C:\Users\Homes\Desktop\FASTAPI\patients.json", "r") as f:
        data = json.load(f)
    return data    

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)    

@router.post("/create")
def create_data(patient: Patient):

    # Load existing data
    data =load_data()
    
   # check if patient ID already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient ID already exists")

    # new patient add database
    data[patient.id] = patient.model_dump(exclude={'id'})

    # Save updated data back to the file
    save_data(data)


    return JSONResponse(status_code=201, content={'message': 'patient Create successfully'})