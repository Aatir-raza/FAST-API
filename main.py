
from fastapi import FastAPI
from patients import router as patients_router
from post_operation import router as post_operation_router

app = FastAPI()

# Connect patients.py
app.include_router(patients_router)
app.include_router(post_operation_router)


@app.get("/")
def hello():
    return {"message": "AATIR RAZA"}


@app.get("/about")
def about():
    return {
        "message": "This is a FastAPI application created by AATIR RAZA."
    }
