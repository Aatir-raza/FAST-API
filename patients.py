
from fastapi import APIRouter, Path, HTTPException 
import json

router = APIRouter()


# Function to load patient data
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


# View all patients
@router.get("/view")
def view():
    data = load_data()
    return data


# View a specific patient
@router.get("/patients/{patient_id}")
def view_patient(patient_id: str =Path(...,description="The ID of the patient to retrieve",example="P001")):

    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")
