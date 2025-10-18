from flask import Flask, request, send_file, render_template
from io import BytesIO
from audio_utils import audio_to_text, text_to_audio
from agent import AIAgent
from google_calendar import GoogleCalendar

app = Flask(__name__)

calendar_service = GoogleCalendar()
ai_agent = AIAgent(calendar_service)

@app.route('/')
def index():
    return render_template("index_2.html")

@app.route('/interact', methods=['POST'])
def interact():
    audio_file = request.files['audio_data']
    text_input = audio_to_text(audio_file)
    response_text = ai_agent.interact(text_input)
    audio_bytes = text_to_audio(response_text)

    return send_file(BytesIO(audio_bytes), mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=True)
