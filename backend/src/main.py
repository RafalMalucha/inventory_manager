from fastapi import FastAPI
# from .core.database import engine, Base
from fastapi.responses import HTMLResponse
#from .routes import auth, inventory, data

# Initialize FastAPI app
app = FastAPI(
    title="Inventory Management API",
    description="A lightweight inventory system with authentication and file handling.",
    version="1.0.0",
)

# Create database tables
# Base.metadata.create_all(bind=engine)

# Register API routes
# app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
# app.include_router(inventory.router, prefix="/api/inventory", tags=["Inventory"])
# app.include_router(data.router, prefix="/api/data", tags=["Data"])

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>test</title>
    </head>
    <body>
        <h1>test</h1>
    </body>
    </html>
    """
