from datetime import timedelta
import google.generativeai as genai

class AIAgent:
    def __init__(self, calendar_service):
        self.calendar_service = calendar_service
        genai.configure(api_key="AIzaSyCWn-vFX_8QUrjG4pK8sQTJasiOp5v8JWE")
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def interact(self, user_input):
        prompt = (
        "Extract the date, time, and duration from this user input. "
        "You MUST respond ONLY with a valid JSON object following this exact format, "
        "with no extra text or explanation:\n"
        "{\"date\": \"YYYY-MM-DD\", \"time\": \"HH:MM\", \"duration\": minutes}\n"
        f"Input: {user_input}\n"
        "Respond only with the JSON object."
        "If date or time are missing in the input, set them to null in the JSON response."
        )

        response = self.model.generate_content(prompt)
        # Add this debug print to see the model's raw output
        # print("Model output for inspection:", response.text)
        print(f"Raw response text:\n{repr(response.text)}")
        # return response.text 

        import json
        try:
            ##
            import re
            import json

            raw_text = response.text.encode('utf-8').decode('unicode_escape')
            pattern = re.compile(r'\{.*\}')
            match = pattern.search(raw_text)
            if match:
                json_text = match.group(0)
                try:
                    result = json.loads(json_text)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    return "Error decoding JSON"
            else:
                print("No JSON object found in response")
                return "No JSON object found in response"

            date_str = result.get('date')
            time_str = result.get('time')
            duration_minutes = result.get('duration')

            if date_str and time_str and duration_minutes is not None:
                from datetime import datetime, timedelta

                # Parse date and time into a single datetime object representing the start time
                start_dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

                # Duration as a timedelta
                duration = timedelta(minutes=int(duration_minutes))

                # Calculate end time by adding duration to start time
                end_dt = start_dt + duration
                message = self.schedule_meeting(start_dt, end_dt, duration)
                return {'text_response': message}  # <-- always return dict
            else:
                missing_parts = []
                if not date_str:
                    missing_parts.append("date")
                if not time_str:
                    missing_parts.append("time")
                if duration_minutes is None:
                    missing_parts.append("duration")
                if missing_parts:
                    message = f"Missing information: {', '.join(missing_parts)}. Please provide complete details."
                    return {'text_response': message}  # <-- return dict instead of string      

        except Exception as e:
            print(f"Error parsing GPT response: {e}")
            return "Error parsing GPT response"

    def schedule_meeting(self, start_dt, end_dt, duration):
        event = {
            'summary': 'Meeting',
            'start': {
                'dateTime': start_dt.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end_dt.strftime('%Y-%m-%dT%H:%M:%S'),
                'timeZone': 'America/Los_Angeles',
            },
        }
    
        event_url = self.calendar_service.create_event(
            event['summary'], 
            event['start']['dateTime'], 
            event['end']['dateTime']
        )
    
        # Build a message for the webpage
        if event_url:
            message = (f"Meeting scheduled from {start_dt.strftime('%Y-%m-%d %H:%M')} "
                       f"to {end_dt.strftime('%Y-%m-%d %H:%M')} ({duration}). "
                       f"Click here to view: {event_url}")
        else:
            message = f"Meeting scheduled from {start_dt.strftime('%Y-%m-%d %H:%M')} " \
                      f"to {end_dt.strftime('%Y-%m-%d %H:%M')} ({duration})."
    
        return message





