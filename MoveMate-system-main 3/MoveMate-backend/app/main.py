from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, favorites, quotes, moves, services, schedules,reviews,login
from .database import Base, engine


Base.metadata.create_all(bind=engine) # create tables in the DB

app = FastAPI()

# CORS Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #TODO: Update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(users.router, prefix="/api", tags=["Users"])
app.include_router(favorites.router, prefix="/api", tags=["Favorites"])
app.include_router(quotes.router, prefix="/api", tags=["Quotes"])
app.include_router(moves.router, prefix="/api", tags=["Moves"])
app.include_router(services.router, prefix="/api", tags=["Services"])
app.include_router(schedules.router, prefix="/api", tags=["Schedules"])
app.include_router(reviews.router, prefix="/api", tags=["Reviews"])
app.include_router(login.router, prefix="/users", tags=["Users"])



# Root endpoint
@app.get("/")
def read_root():
    return {"message": "This is a MoveMate API!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
