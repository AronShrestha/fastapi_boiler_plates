from sqlalchemy.orm import Session

from database.model import course_model
from database.pydantic_schema import course_schema

def get_course(db: Session, course_id: int):
    return db.query(course_model.Course).filter(course_model.Course.id == course_id).first()



def get_courses(db: Session):
    return db.query(course_model.Course).all()


def get_user_courses(user_id : int, db:Session):
    courses = db.query(course_model.Course).filter(course_model.Course.user_id == user_id).all()
    return courses
    
def create_course(db: Session, course: course_schema.CourseCreate):

    db_course = course_model.Course(title = course.title,
                                    description = course.description,
                                    user_id = course.user_id
                                    )
    db.add(db_course )
    db.commit()
    db.refresh(db_course )
    return db_course 