from pydantic import BaseModel

class ComplaintCreate(BaseModel):
    description:str 


class ComplaintResponse(BaseModel):
    id:int 
    description: str
    status:str 
    student_email:str

    class Config:
        from_attributes=True