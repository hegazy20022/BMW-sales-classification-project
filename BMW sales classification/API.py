#!/usr/bin/env python
# coding: utf-8

# In[5]:


from fastapi import FastAPI
from pydantic import BaseModel
import joblib


# In[7]:


model = joblib.load("nb_pipeline.pkl")

app = FastAPI(title="BMW car class API")

class CarFeatures(BaseModel):
    Model: object
    Year: float
    Region: object
    Color: object
    Fuel_Type: object
    Transmission: object
    Engine_Size_L: float
    Mileage_KM: int
    Price_USD: int
    Sales_Volume: int


@app.post("/predict")
def predict(features: CarFeatures):
    input_data = np.array([[value for value in features.dict().values()]])

    prediction = model.predict(input_data)[0]

    return {"prediction": int(prediction)}


# In[ ]:




