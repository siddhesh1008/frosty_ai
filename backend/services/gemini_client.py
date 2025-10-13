# ==========================================================
# backend/services/gemini_client.py
# ----------------------------------------------------------
# Frosty unified Gemini client – fully real-time streaming
# ==========================================================

import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL
import asyncio

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

async def stream_gemini(prompt: str):
    """
    Streams Gemini output token-by-token.
    Uses thread executor for async compatibility.
    """
    try:
        loop = asyncio.get_event_loop()

        def sync_stream():
            for chunk in model.generate_content(prompt, stream=True):
                if chunk.text:
                    yield chunk.text

        # ✅ Do not pre-buffer with list(); yield live tokens instead
        queue = asyncio.Queue()

        def produce():
            try:
                for token in sync_stream():
                    asyncio.run_coroutine_threadsafe(queue.put(token), loop)
            finally:
                asyncio.run_coroutine_threadsafe(queue.put(None), loop)

        # Run producer in background thread
        asyncio.get_running_loop().run_in_executor(None, produce)

        # Consume tokens asynchronously
        while True:
            token = await queue.get()
            if token is None:
                break
            yield token

    except Exception as e:
        print("❌ Error in stream_gemini:", e)
        yield f"❌ Error: {str(e)}"
