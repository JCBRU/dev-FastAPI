from sqlalchemy.orm import Session

import models, schemas

def get_cdr_svi(db: Session, cdr_svi_id: int):
    return db.query(models.CdrSvi).filter(models.CdrSvi.id == cdr_svi_id).first()

def get_cdr_svis(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CdrSvi).offset(skip).limit(limit).all()

def get_cdr_out(db: Session, cdr_out_id: int):
    return db.query(models.CdrOut).filter(models.CdrOut.id == cdr_out_id).first()

def get_cdr_outs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CdrOut).offset(skip).limit(limit).all()

# def get_cdr_svi_by_num(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item