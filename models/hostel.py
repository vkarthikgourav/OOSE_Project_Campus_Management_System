from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class HostelApplication(Base):
    __tablename__="hostel_applications"

    id=Column(Integer,primary_key=True,index=True)
    
    status=Column(String, default="pending")
    room_no=Column(String, nullable=True)

    student_id=Column(Integer,ForeignKey("users.id"))
    student=relationship("User")


class Room(Base):
    __tablename__="rooms"
    id=Column(Integer, primary_key=True, index=True)
    room_no=Column(String, unique=True)
    status=Column(String, default="available")