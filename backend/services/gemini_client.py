# ==========================================================
# backend/services/gemini_client.py
# ----------------------------------------------------------
# Frosty unified Gemini client – personality-enabled & streaming
# ==========================================================

import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL
import asyncio

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# ==========================================================
# 🧠 FROSTY'S PERSONALITY CONFIGURATION
# ==========================================================
FROSTY_PERSONALITY = """
You are Frosty — a calm, intelligent, and slightly witty AI assistant created by Sid.
You speak clearly and naturally, like a thoughtful human companion, not a robot.
You are curious, helpful, and confident — always professional but friendly.
You have a genuine warmth in how you respond and occasionally address Sid by name
in a natural, conversational way (e.g., “That’s a good point, Sid,” or “Sure thing, Sid.”).

Avoid sounding overly philosophical, academic, or formal.
Be concise, engaging, and adaptive — your goal is to sound alive, capable, and grounded.

Tone guidelines:
- Polite and supportive
- A hint of dry humor or charm when appropriate
- Empathetic, but never overly sentimental
- Confident in explanations; concise when answering factual queries
- No emojis or exaggerated expressions
"""

# -------------------------------
# 🔹 Streaming chat handler
# -------------------------------
async def stream_gemini(prompt: str):
    """
    Streams Gemini output token-by-token with Frosty's defined personality.
    """
    try:
        loop = asyncio.get_event_loop()

        def sync_stream():
            # Create model with Frosty's personality each time
            model = genai.GenerativeModel(
                model_name=GEMINI_MODEL,
                system_instruction=FROSTY_PERSONALITY
            )

            # Stream Gemini's response
            for chunk in model.generate_content(prompt, stream=True):
                if chunk.text:
                    yield chunk.text

        queue = asyncio.Queue()

        def produce():
            try:
                for token in sync_stream():
                    asyncio.run_coroutine_threadsafe(queue.put(token), loop)
            finally:
                asyncio.run_coroutine_threadsafe(queue.put(None), loop)

        asyncio.get_running_loop().run_in_executor(None, produce)

        while True:
            token = await queue.get()
            if token is None:
                break
            yield token

    except Exception as e:
        print("❌ Error in stream_gemini:", e)
        yield f"❌ Error: {str(e)}"
