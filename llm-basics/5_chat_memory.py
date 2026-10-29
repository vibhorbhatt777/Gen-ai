# "Memory"
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

#load .env file from parent directory
load_dotenv(r"C:\Code\gen-ai\.env")

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

response_1 = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Hi! i am Vibhor"
)

print("🤖 Assistant:", response_1.text)

# ok now let ask the folloow up questions
response_2 = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What's my name?"
)

print("🤖 Assistant:", response_2.text)
# it give this response = 🤖 Assistant: I don't know your name, as we haven't been introduced! What would you like me to call you?


#every call to llm is completly STATELESS. its totalyy a new call , every single time , As as AI Engineer  , to give the llm "memory".

#build conversations history using types.Content
messages  = [
    types.Content(
        role="user",
        parts=[types.Part(text="Hi! I'm Vibhor!")]

    ),
    types.Content(
        role="model",
        parts=[types.Part(text="Hi Vibhor! how can i assist you today?")]
    ),
    types.Content(
        role="user",
        parts=[types.Part(text="what's my name?")]
    )

]
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=messages
)
print("Assistant:", response.text)
