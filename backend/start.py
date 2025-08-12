import uvicorn
import os

if __name__ == "__main__":
    # Set environment variables for development
    os.environ["DATABASE_URL"] = "sqlite:///./urban_guard.db"
    
    # Start the FastAPI server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )