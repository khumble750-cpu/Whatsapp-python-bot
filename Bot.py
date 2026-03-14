from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "WhatsApp Bot Running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Message received:", data)

    return "OK"

if __name__ == "__main__":
    app.run()# Whatsapp-python-bot
