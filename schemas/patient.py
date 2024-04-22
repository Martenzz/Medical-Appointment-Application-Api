from pydantic import BaseModel



class PatientDetail(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int
    sex: str
    weight: float
    height: float
    phone_number: str


class PatientCreate(PatientDetail):
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "username": "example",
                "first_name": "Zamar",
                "last_name": "Zakari", 
                "age": 18,
                "sex": "male",
                "weight": 75,
                "height": 1.5,
                "phone_number": "+2347036946046",
                "password": "password"
            }
        }

class Patient(PatientCreate):
    id: int



patients: list[Patient] = []
