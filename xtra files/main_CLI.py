# filepath: c:\Users\sarva\OneDrive\Documents\Data_Science_Sarvagya\Projects\ai-agent-calendar\src\main.py
from agent import AIAgent
from google_calendar import GoogleCalendar 

def main():
    calendar_service = GoogleCalendar()
    ai_agent = AIAgent(calendar_service)
    print("Welcome to the AI Calendar Assistant!")
    
    while True:
        user_input = input("How can I assist you today? (type 'exit' to quit) ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = ai_agent.interact(user_input)
        print(response)
        

if __name__ == "__main__":
    main()