import os
from flask import Flask, request
import telebot

# Лучше через переменные окружения в Railway/Render -> Variables
TOKEN   = os.getenv("BOT_TOKEN", "8422200347:AAHaZVamZj8N2qCvKQfaR2y7HJVr08Qkgj0")
CHAT_ID = os.getenv("CHAT_ID",  "5900038402")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Health-check
@app.get("/")
def root():
    return "OK", 200

# Приём данных от ESP
@app.post("/update")
def update():
    device_id   = request.form.get("device_id")
    temperature = request.form.get("temperature")
    bot_token   = request.form.get("bot_token")

    if not (device_id and temperature and bot_token):
        return "Missing params", 400

    if bot_token != TOKEN:
        return "Invalid bot token", 403

    try:
        t = float(temperature)
    except:
        return "Bad temperature", 400

    msg = f"🌡 {device_id}: {t:.1f}°C"
    if t > 30.0:
        msg += "\n⚠️ ВЫСОКАЯ ТЕМПЕРАТУРА"
    elif t < 10.0:
        msg += "\n⚠️ НИЗКАЯ ТЕМПЕРАТУРА"

    bot.send_message(CHAT_ID, msg)
    return "OK", 200

