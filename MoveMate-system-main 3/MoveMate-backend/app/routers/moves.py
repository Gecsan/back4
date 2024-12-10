from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter()

@router.get("/moves/", response_model=list[schemas.Move])
def read_moves(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_moves(db, skip=skip, limit=limit)

@router.get("/moves/{move_id}", response_model=schemas.Move)
def read_move(move_id: int, db: Session = Depends(get_db)):
    db_move = crud.get_move_by_id(db, move_id=move_id)
    if db_move is None:
        raise HTTPException(status_code=404, detail="Move not found")
    return db_move

@router.post("/moves/", response_model=schemas.Move)
def create_move(move: schemas.MoveCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_move(db=db, move=move, user_id=current_user.id)
