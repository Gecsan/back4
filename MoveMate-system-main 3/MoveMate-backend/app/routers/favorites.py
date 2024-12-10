from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db
from ..dependencies import get_current_user
router = APIRouter()


@router.get("/favorites/", response_model=list[schemas.Favorite])
def read_favorites(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_favorites(db, user_id=current_user.id)

@router.post("/favorites/", response_model=schemas.Favorite)
def add_favorite(favorite: schemas.FavoriteCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.add_favorite(db=db, user_id=current_user.id, city_name=favorite.city_name)

@router.delete("/favorites/{favorite_id}", response_model=schemas.Favorite)
def delete_favorite(favorite_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.delete_favorite(db=db, user_id=current_user.id, favorite_id=favorite_id)
