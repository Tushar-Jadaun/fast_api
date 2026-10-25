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
