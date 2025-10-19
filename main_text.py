# new main_text.py
from flask import Flask, render_template, request, jsonify
from agent import AIAgent
from google_calendar import GoogleCalendar

app = Flask(__name__)

calendar_service = GoogleCalendar()
ai_agent = AIAgent(calendar_service)

@app.route('/')
def index():
    return render_template("text.html")

@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json()
    text_input = data.get('text_input', '')
    result = ai_agent.interact(text_input)
    return jsonify(result)