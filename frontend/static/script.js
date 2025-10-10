/* ==========================================================
   Frosty AI Assistant – frontend/static/script.js
   ----------------------------------------------------------
   Version: Streaming (Gemini live responses)
   Works with:
   - index.html  ✅
   - backend/routes/chat_stream.py ✅
   ========================================================== */

document.addEventListener("DOMContentLoaded", () => {
  // ----------------------------
  // 1. DOM Element References
  // ----------------------------
  const chatContainer = document.querySelector("#chat-box");
  const inputField = document.querySelector("#user-input");
  const sendButton = document.querySelector("#send-btn");

  if (!chatContainer || !inputField || !sendButton) {
    console.error("❌ Missing chat elements. Check IDs in HTML.");
    return;
  }

  // ----------------------------
  // 2. Utility Functions
  // ----------------------------

  // Append a message bubble
  function appendMessage(sender, text, isTyping = false) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add(sender === "user" ? "user-msg" : "bot-msg");

    if (isTyping) {
      msgDiv.innerHTML = `<span class="typing-dots"><span>.</span><span>.</span><span>.</span></span>`;
    } else {
      msgDiv.innerHTML = text;
    }

    chatContainer.appendChild(msgDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return msgDiv;
  }

  // Smooth typing animation (optional for small texts)
  async function typeEffect(text, element) {
    element.innerHTML = ""; // clear
    for (let i = 0; i < text.length; i++) {
      element.innerHTML += text.charAt(i);
      await new Promise((resolve) => setTimeout(resolve, 15));
    }
  }

  // ----------------------------
  // 3. Send Message (Streaming)
  // ----------------------------
  async function sendMessage() {
    const userText = inputField.value.trim();
    if (!userText) return;

    // Display user message
    appendMessage("user", userText);
    inputField.value = "";

    // Create an empty bot message bubble
    const botMsg = appendMessage("bot", "");
    let collected = "";

    try {
      // POST to /api/chat/stream (SSE)
      const response = await fetch("/api/chat/stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });

      if (!response.ok || !response.body) {
        throw new Error(`HTTP ${response.status}`);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      let buffer = "";

      // Read Gemini stream chunks
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        // Split by SSE events
        const parts = buffer.split("\n\n");
        buffer = parts.pop(); // keep unfinished event

        for (const part of parts) {
          if (part.startsWith("data:")) {
            const text = part.replace("data:", "").trim();
            if (text === "[DONE]") break;

            // Add streamed text in real-time
            collected += text;
            botMsg.innerHTML = collected + `<span class="cursor">▌</span>`;
            chatContainer.scrollTop = chatContainer.scrollHeight;
          }
        }
      }

      // Remove blinking cursor at end
      botMsg.innerHTML = collected;

    } catch (error) {
      console.error("❌ Stream error:", error);
      botMsg.innerHTML = "⚠️ Unable to reach Frosty right now.";
    }
  }

  // ----------------------------
  // 4. Event Listeners
  // ----------------------------
  sendButton.addEventListener("click", sendMessage);
  inputField.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  // ----------------------------
  // 5. Optional Intro Message
  // ----------------------------
  // Comment this out if your HTML already shows Frosty's intro
  // appendMessage("bot", "👋 Hello, I’m Frosty — your AI assistant.");
});
