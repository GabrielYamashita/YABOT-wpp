import random
from datetime import datetime
from flask import Flask, request, redirect, url_for
from twilio.twiml.messaging_response import MessagingResponse
from msgAnswer import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/yabot", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')
    resp = MessagingResponse()
    user="Yama"

    horario = 0
    addFlag = False

    if msg.lower() in ["oie","oi", "ola", "alo", "alou", "eae", "salve"]:
        resp.message(random.choice([f"Oi {user}!", "Oiee", f"Salve {user}!", f"Eae {user}, tudo bem?"]))

    if msg.lower() in ["user"]:
        user = msg.lower()
        resp.message(f"Hello {user}")

    return str(resp)



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

if __name__ == "__main__":
    app.run(debug=True)
