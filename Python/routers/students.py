from fastapi import APIRouter
import uuid
from models.student import StudentCreate, Student
from datebase import student_db
from typing import List

router = APIRouter(prefix="/students")


@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    id = uuid.uuid4()
    new_student = Student(
        id=id, name=student.name, age=student.age, course=student.course
    )
    student_db.append(new_student)

@router.get("/", response_model=List[Student])
def get_all_students():
    return student_db
    