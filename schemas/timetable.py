from pydantic import BaseModel


class TimetableCreate(BaseModel):
    subject: str
    day: str
    time_slot: str
    teacher_name: str
    class_id: int


class ClassMini(BaseModel):
    id: int
    name: str
    department: str
    semester: int

    class Config:
        from_attributes = True


class TimetableResponse(BaseModel):
    id: int
    subject: str
    day: str
    time_slot: str
    teacher_name: str
    academic_class: ClassMini

    class Config:
        from_attributes = True