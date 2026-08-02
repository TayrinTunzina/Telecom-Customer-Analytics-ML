# FastAPI Code
from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel


# Create API application
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting telecom customer churn",
    version="1.0"
)


# Load trained pipeline

with open(
    "../models/churn_pipeline.pkl",
    "rb"
) as file:

    model = pickle.load(file)

# Define input data format
class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float    

# Prediction Endpoint
@app.post("/predict")
def predict(customer: Customer):

    # Convert input into dataframe

    data = pd.DataFrame(
        [customer.dict()]
    )


    # Prediction

    prediction = model.predict(data)[0]


    if prediction == 1:
        result = "Customer will churn"
    else:
        result = "Customer will stay"


    return {
        "prediction": int(prediction),
        "result": result
    }    


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API is running"
    }