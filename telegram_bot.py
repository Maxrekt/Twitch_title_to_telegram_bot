# telegram_bot.py
import requests

class TelegramBot:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_message(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'
        data = {'chat_id': chat_id, 'text': text}
        response = requests.post(url, data=data)
        response.raise_for_status()
