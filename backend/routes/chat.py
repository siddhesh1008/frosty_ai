# backend/routes/chat.py
"""
FastAPI route for handling chat requests.
Receives text from the frontend, calls Gemini, and returns AI's reply.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.gemini_client import ask_gemini

router = APIRouter(prefix="/api", tags=["Chat"])

# ----------------------------------------------------------
# Define the expected request body schema
# ----------------------------------------------------------
class ChatRequest(BaseModel):
    message: str  # User's message text


# ----------------------------------------------------------
# POST endpoint: /api/chat
# ----------------------------------------------------------
@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Handles chat messages from the frontend and returns Gemini's response.
    """
    try:
        user_message = request.message.strip()
        if not user_message:
            raise HTTPException(status_code=400, detail="Empty message.")

        # Ask Gemini for a reply
        gemini_reply = ask_gemini(user_message)

        # Return JSON to frontend
        return {"response": gemini_reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
