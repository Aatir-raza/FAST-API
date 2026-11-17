
from fastapi import APIRouter, Path, HTTPException, Query
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

@router.get('/sort')
def sort_patients(sort_by: str = Query(..., description='sort on the basis of height, weight, or bmi'),order: str = Query('asc', description='sort order, can be asc or desc')):
    data = load_data()
    valid_fields= ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid fields select from  {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order, select from 'asc' or 'desc'")

    data=load_data()
    sort_order = True if order == 'desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x[sort_by],reverse=sort_order)

    return sorted_data