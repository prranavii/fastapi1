from typing import Optional
from pydantic import BaseModel

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    height: Optional[float] = None
    weight: Optional[float] = None


@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info["id"] = patient_id

    patient_pydantic_object = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_object.model_dump(
        exclude={"id"}
    )

    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={"message": "Patient updated"}
    )

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    del data[patient_id]

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={"message": "Patient deleted"}
    )