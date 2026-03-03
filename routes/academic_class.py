from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.academic_class import AcademicClass
from schemas.academic_class import ClassCreate, ClassResponse
from core.dependencies import require_role

router = APIRouter()

# Admin creates class
@router.post("/class/add", response_model=ClassResponse)
def create_class(
    new_class: ClassCreate,
    user = Depends(require_role("admin")),
    db: Session = Depends(get_db)
):
    obj = AcademicClass(**new_class.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


# View all classes
@router.get("/classes", response_model=list[ClassResponse])
def view_classes(db: Session = Depends(get_db)):
    return db.query(AcademicClass).all()