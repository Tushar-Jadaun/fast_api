from fastapi import FastAPI 
import json
app = FastAPI()

def load_data():
    with open('pateints.json','r') as f:
        data = json.load(f)
        return data

@app.get("/")
def hello():
    return {'message':'hello tushar'}

@app.get("/data")
def view():
    data = load_data()
    return data


@app.get("/pateints/{patients_id}")
def view_pateints(patients_id:str):
    data = load_data()
    
    if patients_id in data:
        return data[patients_id]
    return {'error':'patient is not found'}
    