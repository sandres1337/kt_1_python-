from fastapi import APIRouter
import uuid
from models.teacher import TeacherCreate, Teacher
from datebase import teacher_db
from typing import List

router = APIRouter(prefix="/teachers")


@router.post("/", response_model=Teacher)
def create_teacher(teacher: TeacherCreate):
    id = uuid.uuid4()
    new_teacher = Teacher(
        id=id, name=teacher.name, age=teacher.age, course=teacher.course
    )
    teacher_db.append(new_teacher)

@router.get("/", response_model=List[Teacher])
def get_all_teachers():
    return teacher_db
