from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app=FastAPI()
model=joblib.load("model.pkl")

class house(BaseModel):
    area:float
    bedrooms:int
    age:int
@app.post("/predict")
def predicts(data:house):
    features=[[data.area,data.bedrooms,data.age]]
    prediction=model.predict(features)
    return {"predicted_price":prediction[0] }
