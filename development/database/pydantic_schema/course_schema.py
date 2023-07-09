from pydantic import BaseModel   
from datetime import datetime
from typing import Annotated, Optional, List


class CourseBase(BaseModel):
    title : str
    description : Optional[str] = None
    user_id : int

    

class CourseCreate(CourseBase):
    ...
    
class Course(CourseBase):
    id : int
    # is_active : bool
    # created_at : datetime
    # updated_at : datetime
 
    
    class Config: #since we are working with sqlAlchemy(ORM) we need to set it to true
        orm_mode = True
        