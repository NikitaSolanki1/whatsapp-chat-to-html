# WhatsApp Chat to HTML Converter 📨➡️🌐

This project converts exported WhatsApp chat text files into a beautifully formatted HTML page. It's useful for archiving, displaying, or sharing conversations in a visual format.

## 📌 Project Purpose

This tool was built to:
- Preserve personal or professional chats in a clean and readable format.
- Visualize chat conversations for documentation or presentation.
- Help developers or non-tech users easily review messages.

## 🚀 Technologies Used

- Python: The core script (`convert_to_html.py`) reads `.txt` chat files and generates an HTML file.
- HTML + CSS: For presenting the chat in a clean UI with floating message bubbles.

## 🛠️ How It Works

1. Export your WhatsApp chat as a `.txt` file.
2. Place it in the same folder as `convert_to_html.py`.
3. Set your name and the receiver’s name in the script:
   ```python
   YOUR_NAME = "Your_name"
   RECEIVER_NAME = "Reciver_name"
4. Run the script:
python convert_to_html.py

5. Open the generated chat_output.html file in your browser.


## ✅ Features
Differentiates sender and receiver messages (right/left alignment).

Skips system messages (e.g., "You deleted this message", "Messages are end-to-end encrypted").

Shows timestamp and sender for each message.

Custom CSS styling for clean visuals.
