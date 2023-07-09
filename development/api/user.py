from typing import Annotated, Optional, List
import fastapi
from fastapi import  Header, Path, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from sqlalchemy.ext.asyncio import AsyncSession


from database.config import get_db, async_get_db
from database.pydantic_schema import user_schema,course_schema
from api.utils.user_utils import get_users,get_user, get_user_by_email, create_user
from api.utils.course_utils import get_user_courses

router = fastapi.APIRouter(prefix='/user')


@router.get("/get-user", response_model=List[user_schema.User])
async def read_user(skip : int=0, limit : int=100, db : Session = Depends(get_db) ):
    users = get_users(db , skip=skip, limit=limit)
    return users


@router.post("/create-user", status_code=201, response_model=user_schema.User )
async def create_new_user(user:user_schema.UserCreate, db : Session = Depends(get_db)):
    user = get_user_by_email(db = db, email =user.email )
    if user:
        raise HTTPException(status_code=400,detail="User with that email already exist")
    else:
        return create_user(db = db, user=user)


@router.get("/read_user/{user_id}", response_model=user_schema.User)
async def read_user(user_id : int, db : AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db = db, user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")

    else: return db_user
    
@router.get("users/{user_id}/courses", response_model=List[course_schema.Course])
async def get_user_course(user_id : int, db :  Session = Depends(get_db)):
    courses = get_user_courses(user_id = user_id, db = db)
    print("Courses", courses)
    if len(courses)==0:
        raise HTTPException(status_code=404,detail="User has no courses")

    else:
        return courses
        