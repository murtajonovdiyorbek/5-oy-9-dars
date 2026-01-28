from pydantic import BaseModel

class DoktorCreate(BaseModel):
    full_name: str
    age: int
    phone_number: str

class DoktorResponse(DoktorCreate):
    id: int

    class Config:
        from_attributes = True

class PatientCreate(BaseModel):
    patient_name: str

class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True