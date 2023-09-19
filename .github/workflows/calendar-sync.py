# step 1: create credential.json
import os, json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime  
import yaml

PRIVATE_KEY_ID = os.getenv('PRIVATE_KEY_ID')
PRIVATE_KEY = os.getenv('PRIVATE_KEY').replace('\\n', '\n')

CREDENTIAL = {
  "type": "service_account",
  "project_id": "dmlab-399501",
  "private_key_id": PRIVATE_KEY_ID,
  "private_key": PRIVATE_KEY,
  "client_email": "gh-workflow@dmlab-399501.iam.gserviceaccount.com",
  "client_id": "102578956959894650919",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gh-workflow%40dmlab-399501.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

json.dump(CREDENTIAL, open('./credential.json', 'w'))

creds = service_account.Credentials.from_service_account_file(
    './credential.json',
    scopes=['https://www.googleapis.com/auth/calendar']
)

service = build('calendar', 'v3', credentials=creds)

print('캘린더 로드 완료')

calendar_id='kmudmlab2023@gmail.com'
time_min = "2019-01-01T00:00:00.000000Z"
events_result = service.events().list(calendarId=calendar_id, timeMin=time_min,
    maxResults=200, singleEvents=False).execute()

removed_cnt = 0
for event in events_result['items']:
    try:
        if event['summary'].startswith('세미나 ('):
            # remove event
            service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()
            removed_cnt += 1
    except KeyError:
        pass

print(f'{removed_cnt}개의 세미나 이벤트를 삭제했습니다.')

add_cnt = 0
with open('_data/seminar.yml') as f:
    items = yaml.load(f, Loader=yaml.FullLoader)
    
    for item in items:
        name = item['presenter']
        date = item['date'] # datetime
        # 18:00 ~ 19:00
        start_time = datetime.datetime.combine(date, datetime.time(18, 0, 0))
        end_time = datetime.datetime.combine(date, datetime.time(19, 0, 0))
        # add to calendar
        event = {
            'summary': f'세미나 ({name})',
            'description': '',
            'start': {
                'dateTime': start_time.isoformat(),
                'timeZone': 'Asia/Seoul',
            },
            'end': {
                'dateTime': end_time.isoformat(),
                'timeZone': 'Asia/Seoul',
            },
        }
        service.events().insert(calendarId=calendar_id, body=event).execute()
        add_cnt += 1
print(f'{add_cnt}개의 세미나 이벤트를 추가했습니다.')

# step 3: remove credential.json

os.remove('./credential.json')