from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field , computed_field
from typing import Annotated    
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str , Field(...,description = "ID of the patient in the DB" , example = ["P001"])]
    name: Annotated[str , Field(...,description = "Name of the patient")]
    city: Annotated[str , Field(...,description = "City where the patient is living")]
    age: Annotated[str , Field(...,gt = 0 , lt = 120 , description = "Age of the patient")]
    gender: Annotated[Literal['male','female','others'] , Field(...,description = "Gender of the patient")]
    height: Annotated[str , Field(...,gt = 0 ,description = "Height of the patient in mtrs")]
    weight: Annotated[str ,Field(...,gt=0, description = "Weight of the patient in kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(float(self.weight) / (float(self.height) ** 2), 2)


    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"