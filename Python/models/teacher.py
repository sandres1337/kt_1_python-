from pydantic import BaseModel
from models.course import Course
from uuid import UUID


class Teacher(BaseModel):
    id: UUID
    name: str
    age: int
    course: Course

class TeacherCreate(BaseModel):
    name: str
    age: int
    course: Course

