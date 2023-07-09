from typing import Annotated

from fastapi import FastAPI, Header, Path, Query
from api import user, section, course
from database.config import engine
from database.model import course_model,user_model

user_model.Base.metadata.create_all(bind=engine)
course_model.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(user.router)
app.include_router(section.router)
app.include_router(course.router)


