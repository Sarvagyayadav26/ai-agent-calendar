import sys
print("main_text.py STARTED")  # Add this as the first line
sys.stdout.flush()

import webbrowser
from threading import Timer
from flask import Flask, render_template, request, jsonify
from agent import AIAgent
from google_calendar import GoogleCalendar

app = Flask(__name__)

try:
    calendar_service = GoogleCalendar()
    print("GoogleCalendar instance created")
    sys.stdout.flush()
except Exception as e:
    print("GoogleCalendar error:", e)
    sys.stdout.flush()

ai_agent = AIAgent(calendar_service)

@app.route('/')
def index():
    return render_template("text.html")
@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json()
    text_input = data.get('text_input', '')
    result = ai_agent.interact(text_input)  # result is now dict with message and event_url
    return jsonify(result)


if __name__ == '__main__':
    port = 5000  # Flask default port
    url = f"http://127.0.0.1:{port}/"
    # Open the browser after a short delay to ensure the server is running
    Timer(1, lambda: webbrowser.open(url)).start()
    app.run(debug=True, port=port)



