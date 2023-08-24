import os
import requests

TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = os.getenv('BASE_URL')
TEAM_ID = os.getenv('TEAM_ID')
BOT_ID = os.getenv('BOT_ID')
COMMIT_MESSAGE = os.getenv('COMMIT_MESSAGE')

def find_channel(keyword:str):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + TOKEN
    }
    res = requests.get(BASE_URL + f'users/{BOT_ID}/teams/{TEAM_ID}/channels', headers=headers).json()
    for channel in res:
        if keyword == channel['display_name']:
            return channel
    for channel in res:
        if keyword == channel['name']:
            return channel
    for channel in res:
        if keyword == channel['id']:
            return channel
    return None

def post_message(channel_id:str, message:str, props:object={}):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + TOKEN
    }
    payload = {
        'channel_id': channel_id,
        'message': message,
        'props': props
    }
    res = requests.post(BASE_URL + 'posts', headers=headers, json=payload)
    return res

if '세미나' in COMMIT_MESSAGE or 'seminar' in COMMIT_MESSAGE.lower():
    post_message(find_channel('seminar')['id'], f'[세미나 업데이트 알림]\n{COMMIT_MESSAGE}\nhttps://kmudmlab.github.io/seminar')