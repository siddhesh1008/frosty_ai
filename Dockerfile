# ---------- 1️⃣ Base Image ----------
FROM python:3.12-slim AS base

# ---------- 2️⃣ Working Directory ----------
WORKDIR /app

# ---------- 3️⃣ Install Dependencies ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- 4️⃣ Copy Source ----------
COPY . .

# ---------- 5️⃣ Expose Port ----------
EXPOSE 8000

# ---------- 6️⃣ Run Server ----------
# "--host 0.0.0.0" makes it reachable via Tailscale
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
