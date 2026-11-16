from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel
from typing import Annotated    
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str , Field(...,description = "ID of the patient in the DB" , example = ["P001"])]
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float

def load_data():
