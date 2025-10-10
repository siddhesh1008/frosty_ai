"""
Handles real-time streaming chat responses from Gemini.
This endpoint uses Server-Sent Events (SSE) to send Gemini's
output progressively to the frontend.
"""

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import google.generativeai as genai
import os
from config.settings import GEMINI_API_KEY, GEMINI_MODEL

router = APIRouter(prefix="/api", tags=["Chat (Stream)"])

# Configure Gemini client
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

# ----------------------------------------------------------
# /api/chat/stream – Gemini Streaming Endpoint
# ----------------------------------------------------------
@router.post("/chat/stream")
async def stream_chat(request: Request):
    """
    Stream Gemini responses as Server-Sent Events (SSE).
    The frontend will display messages as they arrive.
    """
    body = await request.json()
    user_message = body.get("message", "").strip()

    if not user_message:
        return StreamingResponse(iter(["data: Empty message\n\n"]), media_type="text/event-stream")

    def gemini_stream():
        import sys
        try:
            response = model.generate_content(user_message, stream=True)
            for chunk in response:
                if chunk.text:
                    # Yield each text piece and flush buffer
                    text = chunk.text.replace("\n", " ").strip()
                    yield f"data: {text}\n\n"
                    sys.stdout.flush()
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: ❌ Error: {str(e)}\n\n"
            sys.stdout.flush()

    return StreamingResponse(gemini_stream(), media_type="text/event-stream")
