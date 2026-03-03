from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.hostel import HostelApplication, Room
from schemas.hostel import HostelResponse
from core.dependencies import require_role, get_current_user

router=APIRouter()

@router.post("/hostel/apply",response_model=HostelResponse)
def apply_hostel(user=Depends(require_role("student")),db:Session=Depends(get_db)):
    existing=db.query(HostelApplication).filter(
        HostelApplication.student_email==user.get("sub")
    ).first()

    if existing:
        raise HTTPException(status_code=400,detail="Already applied")

    new=HostelApplication(student_email=user.get("sub"))
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.get("/hostel/status",response_model=HostelResponse)
def view_status(user=Depends(require_role("student")), db:Session=Depends(get_db)):
    app=db.query(HostelApplication).filter(
        HostelApplication.student_email==user.get("sub")
    ).first()

    if not app:
        raise HTTPException(status_code=404, detail="No application found")

    return app




#Admin role

@router.post("/hostel/allocate")

def allocate(room_no:str, student_email:str, 
user=Depends(require_role("admin")), db:Session=Depends(get_db)):


    room=db.query(Room).filter(Room.room_no==room_no).first()


    if not room or room.status!="available":
        raise HTTPException(status_code=400, detail="Room not available")

    app=db.query(HostelApplication).filter(
        HostelApplication.student_email==student_email
    ).first()

    app.status="approved"
    app.room_no=room_no

    room.status="occupied"

    db.commit()
    return {"msg":"Room allocated"}


@router.post("/hostel/vacate")
def vacate(student_email:str, user=Depends(require_role("admin")),db:Session=Depends(get_db)):
    app=db.query(HostelApplication).filter(
        HostelApplication.student_email==student_email
    ).first()


    room=db.query(Room).filter(Room.room_no==app.room_no).first()

    app.status="vacated"
    app.room_no=None

    room.status="available"
    db.commit()
    return {"msg":"Room vacated"}