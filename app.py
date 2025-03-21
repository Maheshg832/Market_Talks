from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from signals import generate_signal
from bot import send_message
import pytz
from waitress import serve  

app = Flask(__name__)

scheduler = BackgroundScheduler(timezone=pytz.utc)

def scheduled_signal_generation():
    signal = generate_signal()  
    send_message(f"New Signal: {signal}")

scheduler.add_job(scheduled_signal_generation, 'interval', minutes=1)  
scheduler.start()

@app.route('/')
def home():
    return "MarketTalks App is Running!"

@app.route('/generate_signal', methods=['POST', 'GET'])
def generate_and_send_signal():
    signal = generate_signal()
    send_message(f"New Signal: {signal}")
    return {"status": "success", "signal": signal}, 200

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
