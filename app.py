
from email import message
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Fluxo de Conversa
from ConversationYabot import ConversationFlow


app = Flask(__name__)

# from flask_ngrok2 import run_with_ngrok
# run_with_ngrok(app=app, auth_token='27sah00EdAmv9RxS5teUE849TnL_6TnpnpdEeozsPMpugjVvu')


# Home Page
@app.route("/")
def home():
    return "<h1>Hello World!</h1> Welcome to YABOT!"


# Yabot Wpp
GOOD_BOY_URL = (
    "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1"
    "&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
)

flow = ConversationFlow()

@app.route("/yabot", methods=['GET', 'POST'])
def sms_reply():
    # ENTRADA:
    incomingMessage = request.form

    # --> Mensagem:
    messageBody = incomingMessage.get('Body')

    # --> Media:
    hasMedia = int(incomingMessage.get('NumMedia'))

    contentTypeMedia = incomingMessage.get('MediaContentType0')
    urlMedia = incomingMessage.get('MediaUrl0')


    # SAÍDA:
    # response = f"incomingMessage:\n{incomingMessage} \n\nmessageBody:\n{messageBody} \n\nhasMedia:\n{hasMedia} \n\ncontentTypeMedia:\n{contentTypeMedia} \n\nurlMedia:\n{urlMedia}"
    
    # if hasMedia > 0:
        # response = "Thanks for the image. Here's one for you!"

    # else:
    response = flow.processInput(messageBody, hasMedia)
        

    # ENVIO DE MENSAGEM:
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response)

    if hasMedia > 0:
        msg.media(GOOD_BOY_URL)

    return str(resp)


# Loop Principal
if __name__ == "__main__":
    app.run()
