from typing import Annotated, List
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


from database.config import get_db
from database.pydantic_schema import course_schema
from api.utils import course_utils


router = fastapi.APIRouter(prefix='/course')

@router.get("/get-courses", response_model=List[course_schema.Course])
async def read_courses( db : Session = Depends(get_db)):
    return course_utils.get_courses(db = db)


@router.post("/create-course", response_model=course_schema.Course)
async def create_course_api(course :course_schema.CourseCreate ,db : Session = Depends(get_db)):
    return course_utils.create_course(db = db , course = course)


@router.get("/get-course/{course_id}",response_model=course_schema.Course)
async def read_course(course_id : int, db : Session = Depends(get_db)):
    course = course_utils.get_course(course_id=course_id, db = db)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    else:
        return course
        


@router.patch("/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/{id}/sections")
async def read_course_sections():
    return {"courses": []}
