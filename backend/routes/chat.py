# ==========================================================
# backend/routes/chat.py
# ----------------------------------------------------------
# Frosty Chat API – Always Streaming (fixed async generator)
# ==========================================================

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from backend.services.gemini_client import stream_gemini

router = APIRouter(prefix="/api", tags=["Chat"])

@router.post("/chat")
async def chat_endpoint(request: Request):
    """Always streams Gemini responses (real-time)."""
    try:
        data = await request.json()
        user_message = data.get("message", "").strip()

        if not user_message:
            async def empty_message():
                yield "data: ⚠️ Please enter a message.\n\n"
                yield "data: [DONE]\n\n"
            return StreamingResponse(empty_message(), media_type="text/event-stream")

        async def event_stream():
            async for chunk in stream_gemini(user_message):
                yield f"data: {chunk}\n\n"
            yield "data: [DONE]\n\n"

        # ✅ Must not "return" inside the generator; only here
        response = StreamingResponse(event_stream(), media_type="text/event-stream")
        return response

    except Exception as e:
        print("❌ Chat route error:", e)
        async def error_stream():
            yield f"data: ❌ Error: {str(e)}\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(error_stream(), media_type="text/event-stream")
