from fastapi import FastAPI
from routers.students import router as students_router
from routers.teacher import router as teachers_router
app = FastAPI(title="Student API")
app.include_router(students_router)
app.include_router(teachers_router)

@app.get("/")
def root():
    return {"message": "Welcome to API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
