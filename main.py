
from fastapi import FastAPI
from patients import router

app = FastAPI()

# Connect patients.py
app.include_router(router)


@app.get("/")
def hello():
    return {"message": "AATIR RAZA"}


@app.get("/about")
def about():
    return {
        "message": "This is a FastAPI application created by AATIR RAZA."
    }
