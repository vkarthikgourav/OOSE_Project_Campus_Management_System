from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.complaint import Complaint
from schemas.complaint import ComplaintCreate, ComplaintResponse
from core.dependencies import require_role, get_current_user
from models.user import User

router=APIRouter()

#student is submitting complain

@router.post("/complain/submit", response_model=ComplaintResponse)
def submit_complaint(
    complaint: ComplaintCreate,
    user=Depends(require_role("student")),
    db: Session = Depends(get_db)
):
    #db_user = db.query(User).filter(User.email == user["sub"]).first()

    new = Complaint(
        description=complaint.description,
        student_email=user["sub"]
    )

    db.add(new)
    db.commit()
    db.refresh(new)

    return new

@router.get("/complaints", response_model=list[ComplaintResponse])
def view_all(
    user=Depends(require_role("admin")),
    db:Session=Depends(get_db)

):
    return db.query(Complaint).all()

@router.put("/complaint/update/{id}")
def update_status(
    id:int,
    status:str,
    user=Depends(require_role('admin')),
    db:Session=Depends(get_db)
):
    complaint=db.query(Complaint).filter(Complaint.id==id).first()
    complaint.status=status
    db.commit()
    return {"msg":"Updated"}