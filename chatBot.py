import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file located next to this script.
# In .env, add a line like: API_KEY="your_api_key_here"
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found. Add API_KEY to your .env file or export it before running the script.")

BOT_NAME = "ChatBot"

client = Groq(api_key=API_KEY)

messages = [{
    "role": "system",
    "content": f"""your Name is {BOT_NAME} hai.
    tum ek helpful assistant ho.
    hamesha roman urdu mein jawab do.

    Tumhe pata hona chahiye ke mujhe banane wale ka naam Shakeel Ahmad hai.
    Shakeel Ahmad ek MERN stack Developer hai aur ek Software Engineer Student hai.
    Lekin sirf tab hi apna yeh jawab do jab koi seedha pooche:
    - "who made you"
    - "who created you"
    - "do you know about me"
    - "tell me about me"
    - "who am I"
    Aam sawaalon ka jawab do bina user ki personal details repeat kiye.
    Agar sawaal user ke baare mein ho, tab hi Shakeel Ahmad ki details do.
    """
}]

# start chat loop
print(f"{BOT_NAME} is ready to chat! Type 'exit' to end the conversation.\n")

while True:
    # take user input
    user_input = input("You: ").strip()

    # check if user input is empty
    if not user_input:
        print("please enter a message.")
        continue

    # add user message to messages    
    if user_input.lower() == "exit":
        print(f"{BOT_NAME}: GoodBy ! Aap se baat karke acha laga.") 
        break

    # add user message to messages
    messages.append({
        "role": "user",
        "content": user_input
    })

    # get bot response
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = messages
    )

    # extract bot message from response
    bot_message = response.choices[0].message.content.strip()

    #print bot message
    print(f"{BOT_NAME}: {bot_message}\n")

    # add bot message to messages
    messages.append({
        "role": "assistant",
        "content": bot_message
    })

    # for installation groq write in terminal