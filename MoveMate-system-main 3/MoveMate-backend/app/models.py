from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    quotes = relationship("Quote", back_populates="user")
    moves = relationship("Move", back_populates="user")
    favorites = relationship("Favorite", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Quote(Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    move_type = Column(String, nullable=False)
    move_size = Column(String, nullable=False)
    move_date = Column(DateTime, nullable=False)
    estimate = Column(Float, nullable=True)
    status = Column(String, default="pending")

    # Relationships
    user = relationship("User", back_populates="quotes")
    move = relationship("Move", back_populates="quote")


class Move(Base):
    __tablename__ = 'moves'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    quote_id = Column(Integer, ForeignKey('quotes.id'))
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    move_date = Column(DateTime, nullable=False)
    move_size = Column(String, nullable=False)
    move_type = Column(String, nullable=False)
    status = Column(String, default="pending")
    service_id = Column(Integer, ForeignKey('services.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="moves")
    quote = relationship("Quote", back_populates="move")


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)

     # Relationships
    reviews = relationship("Review", back_populates="service")


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey('services.id'))
    date = Column(DateTime, nullable=False)
    availability = Column(Boolean, nullable=False)
    on_schedule = Column(Boolean, nullable=False)

    service = relationship("Service")


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    city_name = Column(String, nullable=False)

    user = relationship("User", back_populates="favorites")


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    rating = Column(Float, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="reviews")
    service = relationship("Service", back_populates="reviews")