from fastapi import FastAPI, HTTPException ,Query
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
    raise HTTPException(status_code=404,detail='pateint is not found')


@app.get("/sort")
def sort_patients(sort_by:str = Query(...,description='sort on the basis of height,weight,bmi'),order:str=Query('asc',description='sort by asc or des order')):
    valid_fields = ['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'invalid details select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f'invalid details select from{order}')
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    sorted_order = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    
    return sorted_order


    