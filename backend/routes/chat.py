from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.services.openai_client import ask_openai

router = APIRouter(prefix="/api/chat")

@router.post("")
async def chat_endpoint(request: Request):
    """
    Receives user message and returns Frosty's full response (non-streaming).
    """
    data = await request.json()
    user_message = data.get("message", "")
    if not user_message:
        return JSONResponse({"reply": "⚠️ No message received."})

    reply = await ask_openai(user_message)
    return JSONResponse({"reply": reply})
