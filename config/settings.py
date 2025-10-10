# config/settings.py
"""
Configuration file for Frosty.
Handles environment variables and API keys.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Gemini expects GOOGLE_API_KEY, so read it properly
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Default model name
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
