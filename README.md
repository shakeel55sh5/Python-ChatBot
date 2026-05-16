# ChatBot

This project contains a simple AI chat bot built with Python and the Groq API. The bot uses a system prompt in Roman Urdu and is designed to run locally with a single script.

## Project Structure

- `chatBot.py` - main Python script for the chatbot.
- `.env` - environment file used to store the `API_KEY` required by the Groq client.

## Prerequisites

- Python 3.11+ installed.
- `pip` available for installing packages.
- A Groq API key.

## Setup Steps

1. Clone or copy this folder into your workspace.
2. Create a Python virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required Python packages.

```bash
pip install python-dotenv groq
```

4. Create a `.env` file in the `chatBot/` folder.

```bash
cd chatBot
cat > .env <<'EOF'
API_KEY="your_api_key_here"
EOF
```

5. Replace `your_api_key_here` with your actual Groq API key.

## How the Chat Bot Works

- The script loads the `API_KEY` from `.env` using `python-dotenv`.
- It initializes a `Groq` client with that API key.
- A system prompt is defined in Roman Urdu, telling the bot to reply as a helpful assistant and to provide specific details about the creator only when directly asked.
- The bot enters a loop where it reads user input, sends the conversation history to the Groq `chat.completions.create()` endpoint, and prints the model response.
- Typing `exit` ends the conversation.

## Running the Chat Bot

From the `chatBot/` folder, run:

```bash
python chatBot.py
```

Then type a message, and the bot will respond. Type `exit` to quit.

## Notes

- Keep your API key private and do not commit the `.env` file to version control.
- If the script raises `API_KEY not found`, verify that `.env` exists and contains the `API_KEY` entry.
- The bot uses the `llama-3.1-8b-instant` model in the current code.

## Customization Ideas

- Change the system prompt to adjust bot personality or behavior.
- Add message logging to save a chat history.
- Implement text preprocessing, response filtering, or conversation reset logic.
