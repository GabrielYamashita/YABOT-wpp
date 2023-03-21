
from flask import Flask, request
from flask_ngrok2 import run_with_ngrok
from twilio.twiml.messaging_response import MessagingResponse

# Fluxo de Conversa
# from ConversationYabot import ConversationFlow
# from msgAnswer import *


app = Flask(__name__)
# run_with_ngrok(app=app, auth_token='27sah00EdAmv9RxS5teUE849TnL_6TnpnpdEeozsPMpugjVvu')

# Home Page
@app.route("/")
def hello():
    return "Hello World!"


# Yabot Wpp
# flow = ConversationFlow()
@app.route("/yabot", methods=['POST'])
def sms_reply():
    # Entrada
    incomingMessage = request.form.get('Body').lower()

    # Saída
    # response = flow.processInput(incomingMessage)
    response = 'Oi'

    # Processamento de Envio de Mensagem
    resp = MessagingResponse()

    if incomingMessage in ['oi']:
        resp.message(f"{response}, Yama!")
    # msg.body(response)

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
