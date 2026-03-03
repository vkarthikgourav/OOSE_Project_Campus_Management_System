from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.timetable import Timetable
from schemas.timetable import TimetableCreate, TimetableResponse
from core.dependencies import require_role

router = APIRouter()


@router.post("/timetable/add", response_model=TimetableResponse)
def add_entry(
    entry: TimetableCreate,
    user = Depends(require_role("admin")),
    db: Session = Depends(get_db)
):
    new = Timetable(**entry.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.get("/timetable/view", response_model=list[TimetableResponse])
def view_timetable(
    class_id: int | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Timetable)

    if class_id:
        query = query.filter(Timetable.class_id == class_id)

    return query.all()