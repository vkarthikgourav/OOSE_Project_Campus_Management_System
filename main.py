from fastapi import FastAPI
from database import engine, Base
from routes.user import router as user_router
from routes.auth import router as auth_router
from routes.admins import router as admin_router
from routes.complaint import router as complaint_router
from routes.hostel import router as hostel_router
from routes.academic_class import router as class_router
from routes.timetable import router as timetable_router


app=FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(complaint_router)
app.include_router(hostel_router)
app.include_router(class_router)
app.include_router(timetable_router)


@app.get("/")
def root():
    return {"msg":"Campus Backend Running"}