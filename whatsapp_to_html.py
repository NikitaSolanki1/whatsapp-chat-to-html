YOUR_NAME = "Your_name"         # Your name in the chat
RECEIVER_NAME = "Reciver_name"     # Replace with the receiver's name as seen in the chat

def convert_to_html(input_file, output_file):
    html_head = '''
    <html>
    <head>
        <title>WhatsApp Chat</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #e5ddd5;
                margin: 0;
                padding: 20px;
            }
            .container {
                width: 100%;
                max-width: 700px;
                margin: auto;
            }
            .msg {
                padding: 10px 15px;
                margin: 10px;
                border-radius: 10px;
                clear: both;
                max-width: 70%;
                word-wrap: break-word;
                position: relative;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            }
            .left {
                background-color: #ffffff;
                float: left;
                text-align: left;
            }
            .right {
                background-color: #dcf8c6;
                float: right;
                text-align: left;
            }
            .sender {
                font-weight: bold;
                color: #075e54;
                display: block;
                margin-bottom: 5px;
            }
            .time {
                font-size: 0.75em;
                color: gray;
                text-align: right;
                display: block;
                margin-top: 5px;
            }
        </style>
    </head>
    <body>
    <div class="container">
    <h2>WhatsApp Chat Export</h2>
    '''

    html_tail = '''
    </div>
    </body>
    </html>
    '''

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(html_head)

        for line in lines:
            try:
                if " - " in line and ": " in line:
                    datetime_part, message = line.split(" - ", 1)
                    sender, text = message.split(": ", 1)
                    sender = sender.strip().replace('\u200d', '')
                    text = text.strip()

                    # Skip system messages
                    if sender not in [YOUR_NAME, RECEIVER_NAME]:
                        continue

                    align_class = "right" if sender == YOUR_NAME else "left"

                    out.write(f'''
                    <div class="msg {align_class}">
                        <span class="sender">{sender}</span>
                        {text}<br>
                        <span class="time">{datetime_part}</span>
                    </div>
                    ''')
            except Exception:
                continue

        out.write(html_tail)

# Call the function
convert_to_html("your_chat.txt", "chat_output.html")
