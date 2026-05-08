import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def send_notifications(message):
    """
    Centraliza o envio de alertas para Telegram e WhatsApp.
    """
    # 1. Lógica para Telegram (Reutilizando sua experiência com Scrapers)
    tg_token = os.getenv("TELEGRAM_TOKEN")
    tg_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if tg_token and tg_chat_id:
        try:
            url = f"https://api.telegram.org/bot{tg_token}/sendMessage"
            payload = {"chat_id": tg_chat_id, "text": message}
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            print(f"Erro ao enviar Telegram: {e}")

    # 2. Lógica para WhatsApp (Via Twilio)
    acc_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    
    if acc_sid and auth_token:
        try:
            client = Client(acc_sid, auth_token)
            client.messages.create(
                from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
                body=message,
                to=os.getenv("MEU_WHATSAPP")
            )
        except Exception as e:
            print(f"Erro ao enviar WhatsApp: {e}")