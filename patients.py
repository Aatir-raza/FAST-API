from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get('/')
def hello():
    return {"message": 'patients management system api'}

@app.get('/about')
def about():
    return {"message": 'A fully functional patients management system.'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patients/{patient_id}') 
def view_patient(patient_id: str):
    # Load the data from the JSON file
    data = load_data()   
    if patient_id in data:
        return data[patient_id]
    return {"error": "Patient not found."}