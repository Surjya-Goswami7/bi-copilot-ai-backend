from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai.groq_service import ask_groq

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str

@router.post("/ai")
async def chat_with_ai(request: AIRequest):

    response = ask_groq(request.prompt)

    return {
        "response": response
    }