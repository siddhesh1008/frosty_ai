/* ==========================================================
   Frosty AI Assistant – frontend/static/script.js
   ----------------------------------------------------------
   ⚡ Non-streaming version (optimized for OpenAI)
   ✅ Fast full responses (no spacing issues)
   ✅ Auto-scroll + error handling + greeting
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

    // Create placeholder bot message
    const botMsg = appendMessage("bot", "💭 Thinking...");
    scrollToBottom();

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const data = await response.json();
      botMsg.innerHTML = data.reply || "⚠️ Frosty didn’t reply.";
    } catch (error) {
      console.error("❌ Chat error:", error);
      botMsg.innerHTML = "⚠️ Unable to reach Frosty right now.";
    }

    scrollToBottom();
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
