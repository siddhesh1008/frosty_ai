/* ==========================================================
   Frosty AI Assistant – frontend/static/script.js
   ----------------------------------------------------------
   ✅ Unified streaming version (works with /api/chat)
   ✅ Handles real-time text flow from Gemini
   ✅ Includes auto-scroll + typing cursor
   ========================================================== */

document.addEventListener("DOMContentLoaded", () => {
  const chatContainer = document.getElementById("chat-box");
  const inputField = document.getElementById("user-input");
  const sendButton = document.getElementById("send-btn");

  if (!chatContainer || !inputField || !sendButton) {
    console.error("❌ Missing chat elements in HTML.");
    return;
  }

  /* ------------------------------
     Helper: Auto-scroll to bottom
     ------------------------------ */
  function scrollToBottom() {
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }

  /* ------------------------------
     Helper: Append chat messages
     ------------------------------ */
  function appendMessage(sender, text) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add(sender === "user" ? "user-msg" : "bot-msg");
    msgDiv.innerHTML = text;
    chatContainer.appendChild(msgDiv);
    scrollToBottom();
    return msgDiv;
  }

  /* ------------------------------
     Send message to Frosty backend
     ------------------------------ */
  async function sendMessage() {
    const userText = inputField.value.trim();
    if (!userText) return;

    // Display user's message
    appendMessage("user", userText);
    inputField.value = "";

    // Create an empty bot message bubble for streamed reply
    const botMsg = appendMessage("bot", `<span class="cursor">▌</span>`);
    let fullReply = "";

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText, stream: true }),
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      // Handle streaming (Server-Sent Events)
      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      let buffer = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const parts = buffer.split("\n\n");
        buffer = parts.pop();

        for (const part of parts) {
          if (!part.startsWith("data:")) continue;
          const text = part.replace("data:", "").trim();

          if (text === "[DONE]") break;
          if (text.startsWith("❌ Error")) {
            botMsg.innerHTML = text;
            scrollToBottom();
            return;
          }

          fullReply += text;
          botMsg.innerHTML = fullReply + `<span class="cursor">▌</span>`;
          scrollToBottom();
        }
      }

      botMsg.innerHTML = fullReply || "⚠️ Frosty didn’t reply.";
      scrollToBottom();

    } catch (error) {
      console.error("❌ Chat error:", error);
      botMsg.innerHTML = "⚠️ Unable to reach Frosty right now.";
      scrollToBottom();
    }
  }

  /* ------------------------------
     Event Listeners
     ------------------------------ */
  sendButton.addEventListener("click", sendMessage);
  inputField.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  /* ------------------------------
     Initial Greeting
     ------------------------------ */
  appendMessage("bot", "👋 Hello, I’m Frosty — your AI assistant.");
});
