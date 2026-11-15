from fastapi import FastAPI

app= FastAPI()   
# app is the object of FastAPI class which is used to create the API endpoints and handle requests.

@app.get("/")  # This decorator is used to define a GET endpoint at the root URL ("/").
def hello():
    return {"message": "Hello, World!"}  # This function returns a JSON response with a greeting message when the root URL is accessed.

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}  # This function returns a JSON response with information about the application when the "/about" URL is accessed.