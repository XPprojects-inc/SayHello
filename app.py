import telebot
from flask import Flask, request

TOKEN = "8422200347:AAHaZVamZj8N2qCvKQfaR2y7HJVr08Qkgj0"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ID твоего чата, куда будут приходить уведомления
YOUR_CHAT_ID = 5900038402

devices = {
    "gp1": "Грядка 1",
    "gp2": "Парник",
}

@app.route('/update', methods=['POST'])
def update():
    device_id = request.form.get('device_id')
    temperature = request.form.get('temperature')
    bot_token = request.form.get('bot_token')

    if bot_token != TOKEN:
        return "Invalid bot token", 403

    device_name = devices.get(device_id, "Неизвестное устройство")
    message = f"🌡 {device_name} ({device_id})\nТемпература: {temperature}°C"

    if float(temperature) > 30.0:
        message += "\n⚠️ ВЫСОКАЯ ТЕМПЕРАТУРА!"

    bot.send_message(YOUR_CHAT_ID, message)
    return "OK", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=443, ssl_context=('cert.pem', 'key.pem'))
