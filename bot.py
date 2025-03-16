import requests

TOKEN = "7618137608:AAEcFGuKFnhFt9-yr48h7W3_smOjiVYtRpg"
CHAT_ID = "5169110521"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)
    
    print(response.json())
if __name__ == "__main__":
    send_message("Hello! MarketTalks Bot is Live! 🚀")
