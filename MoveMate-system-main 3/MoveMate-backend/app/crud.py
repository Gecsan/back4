from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

# Hash passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Utility to hash passwords
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        phone_number=user.phone_number,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Retrieve a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Retrieve all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Retrieve  user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Update user
def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.full_name = user.full_name
        db_user.email = user.email
        db_user.phone_number = user.phone_number
        db_user.password = hash_password(user.password)
        db.commit()
        db.refresh(db_user)
    return db_user

# Delete user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


# CRUD for Quote
def get_quotes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Quote).offset(skip).limit(limit).all()

def get_quote_by_id(db: Session, quote_id: int):
    return db.query(models.Quote).filter(models.Quote.id == quote_id).first()

def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

def delete_quote(db: Session, quote_id: int):
    db_quote = get_quote_by_id(db, quote_id)
    if db_quote:
        db.delete(db_quote)
        db.commit()
    return db_quote

# CRUD for Move
def get_moves(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Move).offset(skip).limit(limit).all()

def get_move_by_id(db: Session, move_id: int):
    return db.query(models.Move).filter(models.Move.id == move_id).first()

def create_move(db: Session, move: schemas.MoveCreate, user_id: int):
    db_move = models.Move(**move.dict(), user_id=user_id)
    db.add(db_move)
    db.commit()
    db.refresh(db_move)
    return db_move

def delete_move(db: Session, move_id: int):
    db_move = get_move_by_id(db, move_id)
    if db_move:
        db.delete(db_move)
        db.commit()
    return db_move

# CRUD for Service
def get_services(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Service).offset(skip).limit(limit).all()

def get_service_by_id(db: Session, service_id: int):
    return db.query(models.Service).filter(models.Service.id == service_id).first()

def create_service(db: Session, service: schemas.ServiceCreate):
    db_service = models.Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def delete_service(db: Session, service_id: int):
    db_service = get_service_by_id(db, service_id)
    if db_service:
        db.delete(db_service)
        db.commit()
    return db_service

# CRUD for Schedule
def get_schedules(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Schedule).offset(skip).limit(limit).all()

def get_schedule_by_id(db: Session, schedule_id: int):
    return db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db: Session, schedule_id: int):
    db_schedule = get_schedule_by_id(db, schedule_id)
    if db_schedule:
        db.delete(db_schedule)
        db.commit()
    return db_schedule

# CRUD for Favorite
def get_favorites(db: Session, user_id: int):
    return db.query(models.Favorite).filter(models.Favorite.user_id == user_id).all()

def add_favorite(db: Session, user_id: int, city_name: str):
    db_favorite = models.Favorite(user_id=user_id, city_name=city_name)
    db.add(db_favorite)
    db.commit()
    db.refresh(db_favorite)
    return db_favorite

def delete_favorite(db: Session, user_id: int, favorite_id: int):
    db_favorite = db.query(models.Favorite).filter(models.Favorite.id == favorite_id, models.Favorite.user_id == user_id).first()
    if db_favorite:
        db.delete(db_favorite)
        db.commit()
    return db_favorite

def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(
        service_id=review.service_id,
        user_id=user_id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews_by_service(db: Session, service_id: int):
    return db.query(models.Review).filter(models.Review.service_id == service_id).all()

def get_review_by_user(db: Session, user_id: int, service_id: int):
    return db.query(models.Review).filter(
        models.Review.user_id == user_id,
        models.Review.service_id == service_id
    ).first()
