from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def get_calendar_event():
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar.readonly'])
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=2, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        return "gap"
    
    event = events[0]
    start = datetime.fromisoformat(event['start']['dateTime'])
    now_time = datetime.utcnow()
    gap = (start - now_time).total_seconds() / 3600

    if gap >= 1:
        return "gap"
    title = event['summary'].lower()
    if "commute to work" in title:
        return "commute"
    elif "church" in title:
        return "church"
    else:
        return "none"
