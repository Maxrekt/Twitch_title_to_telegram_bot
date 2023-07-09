import requests
import time
import re

class TwitchAPI:
    def __init__(self, client_id, access_token):
        self.headers = {
            'Client-ID': client_id,
            'Authorization': 'Bearer ' + access_token,
        }
    
    def get_user_id(self, username):
        response = requests.get(f'https://api.twitch.tv/helix/users?login={username}', headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data['data'][0]['id']

    def get_stream_title(self, user_id):
        response = requests.get(f'https://api.twitch.tv/helix/streams?user_id={user_id}', headers=self.headers)
        response.raise_for_status()
        data = response.json()
        if data['data']:
            title = data['data'][0]['title']
            # Delete all words starting with '!'
            title = re.sub(r'!\w+', '', title)
            return title
        else:
            return "Streamer is offline"