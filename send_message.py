import requests
import os

# 從 GitHub Secrets 讀取 Token / Chat ID
TOKEN = os.getenv("7107000163:AAFxhRaTHPwM0uk_W-X-FjyKekbXmvv3Pz0")
CHAT_ID = os.getenv("1915326639")
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)
    print(response.text)

if __name__ == "__main__":
    send_message("Hello from GitHub Actions 🚀")

