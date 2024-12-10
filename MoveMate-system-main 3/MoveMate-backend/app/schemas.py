from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class QuoteBase(BaseModel):
    origin: str
    destination: str
    move_type: str
    move_size: str
    move_date: datetime

    class Config:
        orm_mode = True

class QuoteCreate(QuoteBase):
    pass

class Quote(QuoteBase):
    id: int
    estimate: Optional[float] = None
    status: str

    class Config:
        orm_mode = True


class MoveBase(BaseModel):
    origin: str
    destination: str
    move_size: str
    move_type: str
    move_date: datetime

    class Config:
        orm_mode = True

class MoveCreate(MoveBase):
    pass

class Move(MoveBase):
    id: int
    status: str
    service_id: int

    class Config:
        orm_mode = True


class FavoriteBase(BaseModel):
    city_name: str

    class Config:
        orm_mode = True

class FavoriteCreate(FavoriteBase):
    pass

class Favorite(FavoriteBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    full_name: str
    email: str
    phone_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    quotes: List[Quote] = []
    moves: List[Move] = []
    favorites: List[Favorite] = []
    created_at: datetime

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class ServiceBase(BaseModel):
    service_name: str
    description: str
    price: float

    class Config:
        orm_mode = True

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int

    class Config:
        orm_mode = True


class ScheduleBase(BaseModel):
    provider_id: int
    date: datetime
    availability: bool
    on_schedule: bool

    class Config:
        orm_mode = True

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: int

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    service_id: int
    rating: float
    comment: Optional[str] = None

    class Config:
        orm_mode = True

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
