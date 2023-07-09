# main.py
from twitch_api import TwitchAPI
from telegram_bot import TelegramBot
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

twitch_client_id = config.get('Twitch', 'client_id')
twitch_access_token = config.get('Twitch', 'access_token')
twitch_streamer_username = config.get('Twitch', 'streamer_username')

telegram_bot_token = config.get('Telegram', 'bot_token')
telegram_chat_id = config.get('Telegram', 'chat_id')


def main():
    twitch_api = TwitchAPI(twitch_client_id, twitch_access_token)
    telegram_bot = TelegramBot(telegram_bot_token)
    chat_id = telegram_chat_id

    username = twitch_streamer_username
    user_id = twitch_api.get_user_id(username)
    current_title = twitch_api.get_stream_title(user_id)
    telegram_bot.send_message(chat_id, f'{current_title}')

    while True:
        time.sleep(60)  # Check every minute
        new_title = twitch_api.get_stream_title(user_id)
        if new_title != current_title:
            telegram_bot.send_message(chat_id, f'Stream title changed: {new_title}')
            current_title = new_title


if __name__ == '__main__':
    main()
