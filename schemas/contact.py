from pydantic import BaseModel

class ContactCreate(BaseModel):
    name: str 
    role: str
    department: str 
    phone: str


class ContactResponse(BaseModel):
    id: int
    name: str 
    role: str
    department: str 
    phone: str 

    class Config: 
        from_attributes=True