import webbrowser
from threading import Timer
from flask import Flask, render_template, request, jsonify
from agent import AIAgent
from google_calendar import GoogleCalendar

app = Flask(__name__)

calendar_service = GoogleCalendar()
ai_agent = AIAgent(calendar_service)

@app.route('/')
def index():
    return render_template("text.html")

# @app.route('/interact', methods=['POST'])
# def interact():
#     data = request.get_json()
#     text_input = data.get('text_input', '')
#     response_text = ai_agent.interact(text_input)
#     return jsonify({'text_response': response_text})
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
