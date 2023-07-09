from pydantic import BaseModel   
from datetime import datetime


class UserBase(BaseModel):
    email : str
    role : int
    

class UserCreate(UserBase):
    ...
    
class User(UserBase):
    id : int
    is_active : bool
    created_at : datetime
 
    
    class Config: #since we are working with sqlAlchemy(ORM) we need to set it to true
        orm_mode = True
        