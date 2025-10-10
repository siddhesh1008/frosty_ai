# backend/services/gemini_client.py
"""
This module connects Frosty to Google's Gemini API.
Currently supports text input/output; we'll add streaming later.
"""

import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL

# ----------------------------------------------------------
# 1. Configure the Gemini SDK using your API key
# ----------------------------------------------------------
genai.configure(api_key=GEMINI_API_KEY)

# ----------------------------------------------------------
# 2. Main function to send prompts to Gemini
# ----------------------------------------------------------
def ask_gemini(prompt: str) -> str:
    """
    Sends a text prompt to Gemini and returns its response.

    Args:
        prompt (str): The user's message or query.

    Returns:
        str: Gemini's text response.
    """
    if not GEMINI_API_KEY:
        return "⚠️ Gemini API key not found. Please check your .env file."

    try:
        # Load model (model name is set in .env)
        model = genai.GenerativeModel(GEMINI_MODEL, generation_config={
            "temperature": 0.9,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 1024,
        })

        # Send prompt and get the response
        response = model.generate_content(prompt)

        # Return Gemini's reply text safely
        return response.text if response and hasattr(response, "text") else "⚠️ No response from Gemini."

    except Exception as e:
        # Catch and return any runtime errors for debugging
        return f"❌ Error communicating with Gemini: {str(e)}"
