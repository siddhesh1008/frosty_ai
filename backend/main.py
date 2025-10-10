# backend/main.py
"""
Main entry point for Frosty's FastAPI backend.

This file:
- Initializes the FastAPI app
- Serves the Frosty frontend (HTML, JS, CSS, assets)
- Registers API routes (like /api/chat)
- Enables CORS for web access
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# ----------------------------------------------------------
# 1. Create FastAPI app
# ----------------------------------------------------------
app = FastAPI(
    title="Frosty AI Assistant",
    description="Backend for Frosty – modular AI assistant powered by Gemini",
    version="1.0.0"
)

# ----------------------------------------------------------
# 2. Enable CORS (Cross-Origin Resource Sharing)
# ----------------------------------------------------------
# This allows your frontend (running from any system) to call the backend API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # You can later restrict this to your own domain or IP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------------------------
# 3. Define frontend directory paths
# ----------------------------------------------------------
FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend"

# Mount static file folders (JS, CSS, images)
app.mount("/static", StaticFiles(directory=FRONTEND_DIR / "static"), name="static")
app.mount("/assets", StaticFiles(directory=FRONTEND_DIR / "assets"), name="assets")


# ----------------------------------------------------------
# 4. Serve index.html
# ----------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    """
    Serves Frosty's main web UI (index.html).
    """
    index_path = FRONTEND_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse("<h2>⚠️ Frontend not found.</h2>", status_code=404)
    return HTMLResponse(index_path.read_text())

# ----------------------------------------------------------
# 5. Import and register all API routes
# ----------------------------------------------------------
from backend.routes.chat import router as chat_router
app.include_router(chat_router)
from backend.routes.chat_stream import router as chat_stream_router
app.include_router(chat_stream_router)

# ----------------------------------------------------------
# 6. Health check endpoint
# ----------------------------------------------------------
@app.get("/ping")
async def ping():
    """
    Simple endpoint to verify Frosty backend is running.
    """
    return {"status": "ok", "message": "Frosty backend is active!"}

# ----------------------------------------------------------
# 7. Run manually (used only when debugging outside Docker)
# ----------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
