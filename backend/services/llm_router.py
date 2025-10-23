# ==========================================================
# 🔹 Frosty LLM Router — Hybrid (Local + Cloud)
# ==========================================================
import re
import requests
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# ENVIRONMENT VARIABLES
# -------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Local Llama3 endpoint (Ollama default)
LOCAL_OLLAMA_URL = "http://localhost:11434/api/generate"
LOCAL_MODEL = "llama3:8b"

# Configure OpenAI client
openai_client = openai.AsyncOpenAI(api_key=OPENAI_API_KEY)

# -------------------------
# Heuristic Router
# -------------------------
def is_complex_prompt(prompt: str) -> bool:
    """
    Simple heuristic to decide if prompt should go to OpenAI (cloud)
    or handled locally.
    """
    # Too long or contains reasoning keywords → use GPT-4o
    if len(prompt.split()) > 50:
        return True

    reasoning_keywords = [
        "explain", "why", "how", "analyze", "compare", "imagine",
        "simulate", "design", "plan", "strategy", "evaluate"
    ]
    if any(word in prompt.lower() for word in reasoning_keywords):
        return True

    # Otherwise → local model
    return False


# -------------------------
# LOCAL (Ollama) CALL
# -------------------------
def ask_local_llama(prompt: str) -> str:
    try:
        payload = {"model": LOCAL_MODEL, "prompt": prompt, "stream": False}
        response = requests.post(LOCAL_OLLAMA_URL, json=payload, timeout=60)
        if response.status_code == 200:
            data = response.json()
            # Extract clean model output only
            return data.get("response", "").strip() or "⚠️ No response from local model."
        else:
            return f"❌ Local model error: {response.status_code}"
    except Exception as e:
        return f"❌ Local model failed: {str(e)}"

# -------------------------
# OPENAI CLOUD CALL
# -------------------------
async def ask_openai_cloud(prompt: str) -> str:
    try:
        response = await openai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are Frosty, a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ OpenAI error: {str(e)}"


# -------------------------
# MAIN ROUTER FUNCTION
# -------------------------
async def ask_frosty(prompt: str) -> str:
    """
    Unified entry point — routes request automatically.
    """
    if is_complex_prompt(prompt):
        print("☁️  Using GPT-4o (cloud model)")
        return await ask_openai_cloud(prompt)
    else:
        print("🦙  Using Llama3:8B (local model)")
        return ask_local_llama(prompt)
