from fastapi import FastAPI
from app.api.destinations import router as destination_router

app = FastAPI(
    title="Traxy AI",
    version="0.1.0",
    description="Your AI Mobility Agent"
)

app.include_router(destination_router)

@app.get("/")
async def root():
    return {
        "app": "Traxy AI",
        "version": "0.1.0",
        "status": "Running 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }