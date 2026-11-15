from fastapi import FastAPI
import json

app= FastAPI()   
# app is the object of FastAPI class which is used to create the API endpoints and handle requests.

def load_data():
    with open("patients.json", "r") as file:  # This line opens the "patients.json" file in read mode.
        data = json.load(file)  # This line reads the content of the file and stores it in the variable 'data'.
        return data
    
@app.get("/")  # This decorator is used to define a GET endpoint at the root URL ("/").
def hello():
    return {"message": "Patient Management System API"}  # This function returns a JSON response with a greeting message when the root URL is accessed.



@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}  # This function returns a JSON response with information about the application when the "/about" URL is accessed.

@app.get("/view")
def view():
    data = load_data()
    return data  # This function returns the patient data loaded from the "patients.json" file when the "/view" URL is accessed.