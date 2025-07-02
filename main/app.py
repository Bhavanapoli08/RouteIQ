from fastapi import FastAPI
import uvicorn
import pickle as pkl
from pydantic import BaseModel 



app = FastAPI(debug=True)

class User(BaseModel):
  name: str
  role: str

from pymongo import MongoClient
db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.big_data
collection = db["journey_cost"]

origins = [
    "http://localhost",
    "http://localhost:3000",
]

@app.get("/")
def home():
    return {'text':'Journey Price Prediction'}

@app.post("/predict")
def predict(Distance:int, TypeofVehicle:int):
    model = pkl.load(open("journey_model.pkl","rb"))
    prediction = model.predict([[Distance,TypeofVehicle]])
    output = prediction

    return {"The Journey Price is: {}".format(output)}

if __name__ == "__main__":
    uvicorn.run(app)