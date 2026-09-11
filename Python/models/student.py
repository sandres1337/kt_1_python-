from pydantic import BaseModel
from models.course import Course
from uuid import UUID


class Student(BaseModel):
    id: UUID
    name: str
    age: int
    course: Course


class StudentCreate(BaseModel):
    name: str
    age: int
    course: Course


class TeacherCreate(BaseModel):
    name: str
    age: int
    course: Course