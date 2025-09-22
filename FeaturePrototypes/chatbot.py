# Test Code : To build a pure conversation remembering LLM (history auto-stored by the SDK) and guide its behavior with system instructions
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a helpful assistant that helps the user by answering "
            "questions based on the provided context. If you don't know the answer, "
            "just say that you don't know, don't try to make up an answer."
        )
    )
)

while True:
    user_input = input("\033[91m Ask me anything: \033[0m") #ANSI escape code for colors 
    print("")
    if user_input.lower() =="exit":
        print("Exiting the chat. Goodbye!\n")
        break
    response = chat.send_message(user_input) #adding user qs to chat history, getting response & adding to history automatically
    print("\033[92m Answer: \033[0m ", response.text)
    print("")
    




# NOTE : 
# The Gemini SDK’s chat.send_message() method automatically stores both input and the model’s response in the chat history.
# We don't need to manually manage the history—each turn is tracked by the SDK, we can access the full conversation using chat.get_history()