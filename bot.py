from flask import Flask, request
from telegram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

bot = Bot(token=TOKEN)

@app.route("/ricevi_posizione", methods=["POST"])
def ricevi_posizione():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    ts = data.get("timestamp")

    if lat and lon and ts:
        msg = f"📍 Posizione ricevuta:\n🌐 Lat: {lat}\n🌐 Lon: {lon}\n🕒 {ts}"
        bot.send_message(chat_id=CHAT_ID, text=msg)
        return "OK", 200
    return "Errore", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)