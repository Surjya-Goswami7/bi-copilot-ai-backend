from fastapi import FastAPI

from app.api.upload import router as upload_router


app = FastAPI(
    title="BI Copilot AI",
    version="1.0.0",
    description="AI-powered Business Intelligence Assistant"
)

app.include_router(upload_router)



@app.get("/")
def home():
    return {
        "message": "Welcome to BI Copilot AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "message": "Backend is running successfully!"
    }