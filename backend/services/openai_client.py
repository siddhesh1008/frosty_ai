# ==========================================================
# backend/services/openai_client.py
# ----------------------------------------------------------
# Frosty AI Assistant – OpenAI-powered unified streaming client
# ==========================================================

import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise ValueError("❌ Missing OPENAI_API_KEY in .env")

# Create OpenAI client
client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# ==========================================================
# 🧠 Frosty's Core Personality
# ==========================================================
FROSTY_PERSONALITY = (
    "You are Frosty — Sid’s personal AI assistant. "
    "You are calm, intelligent, and slightly witty. "
    "You speak naturally, like a human companion who knows Sid well. "
    "You are friendly but professional, confident in your explanations, "
    "and occasionally address Sid by name in a natural way. "
    "Avoid sounding robotic or overly academic. Be concise, clear, and engaging."
)

# ==========================================================
# 🔹 Simple OpenAI Chat (Non-Streaming)
# ==========================================================
async def ask_openai(prompt: str):
    """
    Sends a single prompt to OpenAI and returns the full reply.
    Non-streaming version (fast and stable).
    """
    try:
        response = await client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": FROSTY_PERSONALITY},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("❌ Error in ask_openai:", e)
        return f"❌ Error: {str(e)}"
