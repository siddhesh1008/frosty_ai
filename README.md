
<div align="center">
  <img src="https://github.com/user-attachments/assets/ab186003-82ca-49b8-a34e-f5e38cb5ab4a" 
       alt="Frosty Logo" 
       width="600" height="600">
</div>


# ❄️ FROSTY AI Assistant

A browser-based **real-time conversational AI assistant** powered by **Google Gemini 2.5**, built with **FastAPI**, **Vanilla JS**, and **Docker** — optimized for speed, modularity, and remote access on the BOSGAME P5.

---

## 🚀 Features

- ⚡ **Gemini 2.5 Streaming** – Real-time, token-by-token responses using Google’s latest Gemini API.  
- 🧩 **Modular Architecture** – Add voice, camera, or robotics integrations without touching the core.  
- 🖥️ **Beautiful Web UI** – Modern Frosty-themed design with scrolling chat interface and dynamic updates.  
- 🐳 **Dockerized** – Runs fully isolated; auto-restarts on boot.  
- 🌍 **Tailscale Ready** – Securely access Frosty from anywhere on your network.

---

## 🧠 Architecture Overview

```
frosty_ai/
│
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── routes/
│   │   └── chat.py             # /api/chat streaming endpoint
│   ├── services/
│   │   └── gemini_client.py    # Gemini 2.5 real-time streaming logic
│   └── config/
│       └── settings.py         # Loads API keys and config
│
├── frontend/
│   ├── index.html              # Frosty chat UI
│   ├── static/
│   │   ├── style.css           # Interface styling
│   │   └── script.js           # Streaming chat logic
│   └── assets/
│       └── logo.png            # Frosty logo
│
├── .env                        # Gemini API keys (excluded from Git)
├── Dockerfile                  # Docker image definition
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/frosty_ai.git
cd frosty_ai
```

### 2️⃣ Create an `.env` File
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-pro
```

⚠️ *Keep this file private. Do not commit to GitHub.*

---

### 3️⃣ Build & Run with Docker
```bash
sudo docker build -t frosty-ai .
sudo docker run -d \
  --name frosty \
  -p 8000:8000 \
  -v ~/frosty_ai:/app \
  --restart always \
  frosty-ai
```

Then open Frosty in your browser:
```
http://<your-local-ip>:8000
```

If using **Tailscale**:
```
http://<your-tailscale-ip>:8000
```

---

### 4️⃣ Auto-Start Frosty on Boot
```bash
sudo nano /etc/systemd/system/frosty.service
```

Add:
```ini
[Unit]
Description=FROSTY AI Assistant
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a frosty
ExecStop=/usr/bin/docker stop -t 2 frosty

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable frosty
sudo systemctl start frosty
```

---

## 💬 Usage

- Type messages into Frosty’s chat box and press **Enter** or **Send**.  
- Frosty streams Gemini’s response in real-time — just like ChatGPT.  
- Supports multi-line messages, smooth scroll, and typing indicator.  

💡 You can easily extend Frosty with:
- 🎙️ Voice recognition  
- 🔊 Text-to-speech  
- 🧠 Context memory  
- 🤖 ROS integration for robotics projects  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Vanilla JS |
| **Backend** | FastAPI, Uvicorn |
| **AI Model** | Google Gemini 2.5 Pro |
| **Runtime** | Docker |
| **Platform** | BOSGAME P5 (Linux / Ubuntu) |

---

## 📦 Dependencies

```
fastapi
uvicorn
google-generativeai
python-dotenv
```

To install manually:
```bash
pip install -r requirements.txt
```

---

## 🧭 Example Interaction

```
User: Hey Frosty, how are you?
Frosty: I’m running at full power and ready to help, Sid! ⚙️
```

---

## 🌐 Future Plans

- 🎙️ Add mic input (Speech-to-Text)
- 🔊 Add TTS for Frosty’s voice
- 🧠 Implement memory for ongoing context
- 🤖 Link to your AI Rover / ROS system
- 🌍 Deploy via WebSocket or LiveKit for multi-device chat

---

## 👨‍💻 Author

**Siddhesh (Sid)**  
🎓 Master’s in Engineering & Sustainable Management – Industry 4.0, Automation, Robotics & 3D Manufacturing  
📍 Based in Berlin, Germany  

🔗 [LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/)

---

## 🧊 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and expand Frosty — just credit the original creator.

---

✨ *Frosty – Built to think, talk, and assist. Anywhere. Anytime.*

# ❄️ FROSTY AI Assistant

A browser-based **real-time conversational AI assistant** powered by **Google Gemini 2.5**, built with **FastAPI**, **Vanilla JS**, and **Docker** — optimized for speed, modularity, and remote access on the BOSGAME P5.

---

## 🚀 Features

- ⚡ **Gemini 2.5 Streaming** – Real-time, token-by-token responses using Google’s latest Gemini API.  
- 🧩 **Modular Architecture** – Add voice, camera, or robotics integrations without touching the core.  
- 🖥️ **Beautiful Web UI** – Modern Frosty-themed design with scrolling chat interface and dynamic updates.  
- 🐳 **Dockerized** – Runs fully isolated; auto-restarts on boot.  
- 🌍 **Tailscale Ready** – Securely access Frosty from anywhere on your network.

---

## 🧠 Architecture Overview

```
frosty_ai/
│
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── routes/
│   │   └── chat.py             # /api/chat streaming endpoint
│   ├── services/
│   │   └── gemini_client.py    # Gemini 2.5 real-time streaming logic
│   └── config/
│       └── settings.py         # Loads API keys and config
│
├── frontend/
│   ├── index.html              # Frosty chat UI
│   ├── static/
│   │   ├── style.css           # Interface styling
│   │   └── script.js           # Streaming chat logic
│   └── assets/
│       └── logo.png            # Frosty logo
│
├── .env                        # Gemini API keys (excluded from Git)
├── Dockerfile                  # Docker image definition
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/frosty_ai.git
cd frosty_ai
```

### 2️⃣ Create an `.env` File
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-pro
```

⚠️ *Keep this file private. Do not commit to GitHub.*

---

### 3️⃣ Build & Run with Docker
```bash
sudo docker build -t frosty-ai .
sudo docker run -d \
  --name frosty \
  -p 8000:8000 \
  -v ~/frosty_ai:/app \
  --restart always \
  frosty-ai
```

Then open Frosty in your browser:
```
http://<your-local-ip>:8000
```

If using **Tailscale**:
```
http://<your-tailscale-ip>:8000
```

---

### 4️⃣ Auto-Start Frosty on Boot
```bash
sudo nano /etc/systemd/system/frosty.service
```

Add:
```ini
[Unit]
Description=FROSTY AI Assistant
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a frosty
ExecStop=/usr/bin/docker stop -t 2 frosty

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable frosty
sudo systemctl start frosty
```

---

## 💬 Usage

- Type messages into Frosty’s chat box and press **Enter** or **Send**.  
- Frosty streams Gemini’s response in real-time — just like ChatGPT.  
- Supports multi-line messages, smooth scroll, and typing indicator.  

💡 You can easily extend Frosty with:
- 🎙️ Voice recognition  
- 🔊 Text-to-speech  
- 🧠 Context memory  
- 🤖 ROS integration for robotics projects  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Vanilla JS |
| **Backend** | FastAPI, Uvicorn |
| **AI Model** | Google Gemini 2.5 Pro |
| **Runtime** | Docker |
| **Platform** | BOSGAME P5 (Linux / Ubuntu) |

---

## 📦 Dependencies

```
fastapi
uvicorn
google-generativeai
python-dotenv
```

To install manually:
```bash
pip install -r requirements.txt
```

---

## 🧭 Example Interaction

```
User: Hey Frosty, how are you?
Frosty: I’m running at full power and ready to help, Sid! ⚙️
```

---

## 🌐 Future Plans

- 🎙️ Add mic input (Speech-to-Text)
- 🔊 Add TTS for Frosty’s voice
- 🧠 Implement memory for ongoing context
- 🤖 Link to your AI Rover / ROS system
- 🌍 Deploy via WebSocket or LiveKit for multi-device chat

---

## 👨‍💻 Author

**Siddhesh (Sid)**  
🎓 Master’s in Engineering & Sustainable Management – Industry 4.0, Automation, Robotics & 3D Manufacturing  
📍 Based in Berlin, Germany  

🔗 [LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/)

---

## 🧊 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and expand Frosty — just credit the original creator.

---

✨ *Frosty – Built to think, talk, and assist. Anywhere. Anytime.*

# ❄️ FROSTY AI Assistant

A browser-based **real-time conversational AI assistant** powered by **Google Gemini 2.5**, built with **FastAPI**, **Vanilla JS**, and **Docker** — optimized for speed, modularity, and remote access on the BOSGAME P5.

---

## 🚀 Features

- ⚡ **Gemini 2.5 Streaming** – Real-time, token-by-token responses using Google’s latest Gemini API.  
- 🧩 **Modular Architecture** – Add voice, camera, or robotics integrations without touching the core.  
- 🖥️ **Beautiful Web UI** – Modern Frosty-themed design with scrolling chat interface and dynamic updates.  
- 🐳 **Dockerized** – Runs fully isolated; auto-restarts on boot.  
- 🌍 **Tailscale Ready** – Securely access Frosty from anywhere on your network.

---

## 🧠 Architecture Overview

```
frosty_ai/
│
├── backend/
│   ├── main.py                 # FastAPI entry point
│   ├── routes/
│   │   └── chat.py             # /api/chat streaming endpoint
│   ├── services/
│   │   └── gemini_client.py    # Gemini 2.5 real-time streaming logic
│   └── config/
│       └── settings.py         # Loads API keys and config
│
├── frontend/
│   ├── index.html              # Frosty chat UI
│   ├── static/
│   │   ├── style.css           # Interface styling
│   │   └── script.js           # Streaming chat logic
│   └── assets/
│       └── logo.png            # Frosty logo
│
├── .env                        # Gemini API keys (excluded from Git)
├── Dockerfile                  # Docker image definition
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/frosty_ai.git
cd frosty_ai
```

### 2️⃣ Create an `.env` File
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-pro
```

⚠️ *Keep this file private. Do not commit to GitHub.*

---

### 3️⃣ Build & Run with Docker
```bash
sudo docker build -t frosty-ai .
sudo docker run -d \
  --name frosty \
  -p 8000:8000 \
  -v ~/frosty_ai:/app \
  --restart always \
  frosty-ai
```

Then open Frosty in your browser:
```
http://<your-local-ip>:8000
```

If using **Tailscale**:
```
http://<your-tailscale-ip>:8000
```

---

### 4️⃣ Auto-Start Frosty on Boot
```bash
sudo nano /etc/systemd/system/frosty.service
```

Add:
```ini
[Unit]
Description=FROSTY AI Assistant
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a frosty
ExecStop=/usr/bin/docker stop -t 2 frosty

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable frosty
sudo systemctl start frosty
```

---

## 💬 Usage

- Type messages into Frosty’s chat box and press **Enter** or **Send**.  
- Frosty streams Gemini’s response in real-time — just like ChatGPT.  
- Supports multi-line messages, smooth scroll, and typing indicator.  

💡 You can easily extend Frosty with:
- 🎙️ Voice recognition  
- 🔊 Text-to-speech  
- 🧠 Context memory  
- 🤖 ROS integration for robotics projects  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, Vanilla JS |
| **Backend** | FastAPI, Uvicorn |
| **AI Model** | Google Gemini 2.5 Pro |
| **Runtime** | Docker |
| **Platform** | BOSGAME P5 (Linux / Ubuntu) |

---

## 📦 Dependencies

```
fastapi
uvicorn
google-generativeai
python-dotenv
```

To install manually:
```bash
pip install -r requirements.txt
```

---

## 🧭 Example Interaction

```
User: Hey Frosty, how are you?
Frosty: I’m running at full power and ready to help, Sid! ⚙️
```

---

## 🌐 Future Plans

- 🎙️ Add mic input (Speech-to-Text)
- 🔊 Add TTS for Frosty’s voice
- 🧠 Implement memory for ongoing context
- 🤖 Link to your AI Rover / ROS system
- 🌍 Deploy via WebSocket or LiveKit for multi-device chat

---

## 👨‍💻 Author

**Siddhesh (Sid)**  
🎓 Master’s in Engineering & Sustainable Management – Industry 4.0, Automation, Robotics & 3D Manufacturing  
📍 Based in Berlin, Germany  

🔗 [LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/)

---

## 🧊 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and expand Frosty — just credit the original creator.

---

✨ *Frosty – Built to think, talk, and assist. Anywhere. Anytime.*
