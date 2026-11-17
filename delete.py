from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.responses import JSONResponse
import json

router = APIRouter()

@router.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = data_load()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return JSONResponse(
        content={"message": "Patient deleted successfully"},
        status_code=200,
    )

def data_load():
    with open(r"C:\Users\Homes\Desktop\FASTAPI\patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open(r"C:\Users\Homes\Desktop\FASTAPI\patients.json", "w") as f:
        json.dump(data, f)