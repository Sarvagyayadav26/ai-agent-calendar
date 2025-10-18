# AI Agent Calendar

This project implements an AI agent that interacts with users via text and can schedule meetings using Google Calendar.

## Project Structure

```
ai-agent-calendar
├── src
│   ├── main.py          # Entry point of the application
│   ├── agent.py         # Contains the AIAgent class for user interaction
│   ├── calendar.py      # Contains the GoogleCalendar class for calendar operations
│   └── utils.py         # Utility functions for text processing
├── requirements.txt     # Lists the project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-agent-calendar
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up Google Calendar API:
   - Follow the instructions on the [Google Calendar API documentation](https://developers.google.com/calendar/quickstart/python) to create credentials and enable the API.
   - Download the `credentials.json` file and place it in the `src` directory.

## Usage

To run the AI agent, execute the following command:

```
python src/main.py
```

The agent will prompt you for input. You can ask it to schedule meetings by providing details such as date, time, and participants.

## Capabilities

- Interacts with users through natural language processing.
- Schedules meetings in Google Calendar based on user input.
- Handles authentication with Google Calendar API.

## Contributing

Feel free to submit issues or pull requests for improvements and features.