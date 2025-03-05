from fastapi import FastAPI
from .core.database import engine, Base
from .auth.routes import router

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router, prefix="/auth")