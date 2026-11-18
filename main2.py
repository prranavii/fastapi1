
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()


class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient in the DB", examples=["P001"])]

    name: Annotated[str, Field(..., description="Name of the patient")]

    city: Annotated[str, Field(..., description="City where the patient is living")]

    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]

    gender: Annotated[Literal['male', 'female', 'others'], Field(...)]

    height: Annotated[float, Field(..., gt=0, description="Height in meters")]

    weight: Annotated[float, Field(..., gt=0, description="Weight in kgs")]


    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"

        elif self.bmi < 25:
            return "Normal weight"

        elif self.bmi < 30:
            return "Overweight"

        else:
            return "Obesity"


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)


@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()

    for existing_patient in data.values():

        if existing_patient['id'] == patient.id:
            raise HTTPException(
                status_code=400,
                detail="Patient with this ID already exists."
            )

    data[patient.id] = patient.model_dump()

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient created successfully"}
    )
