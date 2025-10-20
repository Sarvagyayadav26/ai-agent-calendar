from flask import Flask, render_template, request, jsonify
from agent import AIAgent
from google_calendar import GoogleCalendar
import os
import json
from google.oauth2.credentials import Credentials
from vercel_wsgi import handle

# Initialize Flask app
app = Flask(__name__)

# Initialize your services
creds_data = os.getenv('GOOGLE_CREDENTIALS')
if not creds_data:
    raise ValueError("GOOGLE_CREDENTIALS environment variable not set")

creds_dict = json.loads(creds_data)
creds = Credentials.from_authorized_user_info(creds_dict)
calendar_service = GoogleCalendar(credentials=creds)
ai_agent = AIAgent(calendar_service)

# Routes
@app.route('/')
def index():
    return render_template("text.html")

@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json()
    text_input = data.get('text_input', '')
    result = ai_agent.interact(text_input)
    return jsonify(result)

# Vercel handler must be at the very end
def handler(request, context=None):
    return handle(app, request, context)
