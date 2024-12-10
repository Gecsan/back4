from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db


router = APIRouter()

@router.get("/schedules/", response_model=list[schemas.Schedule])
def read_schedules(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_schedules(db, skip=skip, limit=limit)

@router.post("/schedules/", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    return crud.create_schedule(db=db, schedule=schedule)
