from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import crud, schemas
from ..database import get_db
from ..dependencies import create_access_token

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", response_model=schemas.Token)
def login(login: schemas.Login, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=login.email)

    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Verify password
    if not pwd_context.verify(login.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    # Create JWT token and return it
    access_token = create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
