from typing import Dict, List

from pydantic import BaseModel

class Patient(BaseModel):  #step 1
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] #used List and not list because List is a generic type provided by the typing module, which allows you to specify the type of elements in the list. In this case, it indicates that allergies is a list of strings. 
    contact_details: Dict[str, str] # used Dict and not dict because Dict is a generic type provided by the typing module, which allows you to specify the types of keys and values in the dictionary. In this case, it indicates that contact_details is a dictionary with string keys and string values.

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')

def update_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')

patient_info = {'name':'john'   , 'age': 30 , 'weight': 70 , 'married': True , 'allergies': ['pollen', 'dust'] , 'contact_details': {'email': 'john@example.com'}, 'phone':'123-456-7890'}


patient1 = Patient(**patient_info)  #step 2 (pydantic object creation)

insert_patient_data(patient1)  #step 3 (passing pydantic object to function)