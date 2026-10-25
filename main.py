from fastapi import FastAPI 
app = FastAPI()

@app.get("/")
def hello():
    return {'message':'hello tushar'}

@app.get("/about")
def hii():
    return{'message':'hello harsh'}
