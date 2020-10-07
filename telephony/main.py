import os

from enum import Enum
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas

from database import DBSession, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()

#cdr_svi
@app.get("/cdr_svi/", response_model=List[schemas.CdrSvi])
def read_cdr_svis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cdr_svis = crud.get_cdr_svis(db, skip=skip, limit=limit)
    return cdr_svis

@app.get("/cdr_svi/{cdr_svi_id}", response_model=schemas.CdrSvi)
def read_cdr_svi(cdr_svi_id: int, db: Session = Depends(get_db)):
    db_cdr_svi = crud.get_cdr_svi(db, cdr_svi_id=cdr_svi_id)
    if db_cdr_svi is None:
        raise HTTPException(status_code=404, detail="Call not found in cdr_svi")
    return db_cdr_svi


# cdr_out
@app.get("/cdr_out/", response_model=List[schemas.CdrOut])
def read_cdr_outs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cdr_outs = crud.get_cdr_outs(db, skip=skip, limit=limit)
    return cdr_outs

@app.get("/cdr_out/{cdr_out_id}", response_model=schemas.CdrOut)
def read_cdr_out(cdr_out_id: int, db: Session = Depends(get_db)):
    db_cdr_out = crud.get_cdr_out(db, cdr_out_id=cdr_out_id)
    if db_cdr_out is None:
        raise HTTPException(status_code=404, detail="Call not found in cdr_out")
    return db_cdr_out
