from flask import Flask, render_template, request, jsonify
from agent import AIAgent
from google_calendar import GoogleCalendar
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

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

@app.route('/')
def index():
    return render_template("text.html")

@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json()
    text_input = data.get('text_input', '')
    result = ai_agent.interact(text_input)
    return jsonify(result)

# ---------------------------
# 👇 This part makes it work on Vercel
def handler(request, context=None):
    from vercel_wsgi import handle
    return handle(app, request, context)
# ---------------------------


