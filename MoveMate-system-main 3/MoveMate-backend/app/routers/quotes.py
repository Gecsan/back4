from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db
from ..dependencies import get_current_user
from ..schemas import Quote

router = APIRouter()

@router.get("/quotes/", response_model=list[Quote])
def read_quotes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_quotes(db, skip=skip, limit=limit)

@router.get("/quotes/{quote_id}", response_model=schemas.Quote)
def read_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = crud.get_quote_by_id(db, quote_id=quote_id)
    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")
    return db_quote

@router.post("/quotes/", response_model=schemas.Quote)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    return crud.create_quote(db=db, quote=quote)
