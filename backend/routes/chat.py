from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.services.llm_router import ask_frosty

router = APIRouter(prefix="/api/chat")

@router.post("")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    if not user_message:
        return JSONResponse({"reply": "⚠️ No message received."})

    reply = await ask_frosty(user_message)
    return JSONResponse({"reply": reply})
