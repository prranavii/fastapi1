from fastapi import FastAPI , Path, HTTPException, Query
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

#path params

@app.get("/patient/{patient_id}")  # This decorator defines a GET endpoint that takes a path parameter 'patient_id'.
def view_patient(patient_id: str = Path(..., description = "ID of the patient in the DB" , example = "P001")):  # This function takes 'patient_id' as a string parameter.
    data = load_data()  # This line loads the patient data from the "patients.json" file.
    if patient_id in data:
        return data[patient_id]  # If the patient ID exists in the data, it returns the corresponding patient record.

    raise HTTPException(status_code=404, detail="Patient not found")  # If the patient ID does not exist, it raises a 404 HTTP exception with a "Patient not found" message.

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = 'sort on the basis of height , weight or bmi ' ), order : str = Query('asc', description = 'asc or desc')):

    valid_fields = ['height', 'weight', 'bmi'] 

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")  # If the 'sort_by' parameter is not valid, it raises a 400 HTTP exception with a message indicating the valid fields.
    
    data = load_data()

    sort_order = True if order == 'desc' else False  # This line determines the sorting order based on the 'order' query parameter. If 'order' is 'desc', it sets 'sort_order' to True; otherwise, it sets it to False.
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse = sort_order)  # This line sorts the patient data based on the specified field and order.
    return sorted_data  # This line returns the sorted patient data as a JSON response.