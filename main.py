from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"message": 'AATIR RAZA'}

@app.get('/about')
def about():
    return {"message": 'This is a FastAPI application created by AATIR RAZA.'}