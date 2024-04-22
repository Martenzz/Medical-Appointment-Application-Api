from pydantic import BaseModel


class DoctorBase(BaseModel):
    username: str
    specialization: str
    phone: str
    is_available: bool = True


    class Config:
        json_schema_extra = {
            "example": {
                "username": "DrMartins",
                "specialization": "Gynecology",
                "phone": "+23470500690",
                "is_available": True,
                "password": "password"
            }
        }


class DoctorCreate(DoctorBase):
    password: str

class Doctor(DoctorBase):
    id: int

doctors: list[Doctor] = []
