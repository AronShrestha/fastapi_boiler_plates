from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select




from database.model import user_model
from database.pydantic_schema import user_schema 


# def get_user(db: Session, user_id: int):
#     return db.query(user_model.User).filter(user_model.User.id == user_id).first()


#making async
async def get_user(db : AsyncSession, user_id : int):
    query = select(user_model.User).where(user_model.User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):

    db_user = user_model.User(email=user.email, role = user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


