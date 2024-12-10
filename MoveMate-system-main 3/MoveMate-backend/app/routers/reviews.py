from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Review)
def submit_review(
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_review = crud.get_review_by_user(db, user_id=current_user.id, service_id=review.service_id)
    if db_review:
        raise HTTPException(status_code=400, detail="Review already submitted for this service")
    return crud.create_review(db=db, review=review, user_id=current_user.id)

@router.get("/service/{service_id}", response_model=list[schemas.Review])
def get_reviews_for_service(service_id: int, db: Session = Depends(get_db)):
    reviews = crud.get_reviews_by_service(db, service_id=service_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for this service")
    return reviews
