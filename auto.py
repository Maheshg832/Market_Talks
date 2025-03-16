import time
from signals import generate_signal
from bot import send_message

while True:
    signal = generate_signal()
    send_message(f"Auto Signal: {signal}")
    print(f"Sent Signal: {signal}")
    time.sleep(300)
