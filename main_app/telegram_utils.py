import requests

TELEGRAM_BOT_TOKEN = "7950489007:AAH_fzIlcfMeXOW4vWA_hR05Z2FEQANnR2o"
TELEGRAM_CHAT_ID = "2040972452"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    return response.json()