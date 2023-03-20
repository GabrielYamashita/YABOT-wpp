
from datetime import datetime
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from msgAnswer import *

# Fluxo de Conversa
from ConversationYabot import ConversationFlow


app = Flask(__name__)

# Home Page
@app.route("/")
def hello():
    return "Hello World!"


# Yabot Wpp
user="Yama"
flow = ConversationFlow()
@app.route("/yabot", methods=['POST'])
def sms_reply():
    # Entrada
    incomingMessage = request.form.get('Body').lower()

    # Saída
    # response = flow.processInput(incomingMessage)
    response = 'oi'

    # Processamento de Envio de Mensagem
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response)

    return str(resp)


# Good Boy
GOOD_BOY_URL = (
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
    "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
)

@app.route("/goodboy", methods=["GET", "POST"])
def reply_whatsapp():
    try:
        num_media = int(request.values.get("NumMedia"))

    except (ValueError, TypeError):
        return "Invalid request: invalid or missing NumMedia parameter", 400

    response = MessagingResponse()

    if not num_media:
        msg = response.message("Send us an image!")
    else:
        msg = response.message("Thanks for the image. Here's one for you!")
        msg.media(GOOD_BOY_URL)

    return str(response)


# Loop Principal
if __name__ == "__main__":
    app.run(debug=True)
