import webbrowser
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
from google.auth.transport.requests import Request
import os
import json
from google.oauth2.credentials import Credentials

class GoogleCalendar:
    # flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
    SCOPES = [
    'https://www.googleapis.com/auth/calendar', 
    'https://www.googleapis.com/auth/calendar.events'
]
    def __init__(self, credentials=None):
        self.creds = None
        self.service = None
        self.authenticate()
        if credentials:
            self.creds = credentials
        else:
            self.creds = None
            self.authenticate()


    #
    def authenticate(self):
        # Load credentials from environment variable
        creds_data = os.getenv('GOOGLE_CREDENTIALS')
        if creds_data:
            creds_dict = json.loads(creds_data)
            self.creds = Credentials.from_authorized_user_info(creds_dict, self.SCOPES)
        
        # Refresh token if expired
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                # Only for local development: interactive flow
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=5000)
        
        # Build the calendar service
        self.service = build('calendar', 'v3', credentials=self.creds)

    
        #
    def create_event(self, summary, start_time, end_time):
        event = {
            'summary': summary,
            'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'},
        }
        created_event = self.service.events().insert(calendarId='primary', body=event).execute()
        event_url = created_event.get('htmlLink')
        webbrowser.open(event_url)  # This opens the link in the user's default browser
        return event_url






