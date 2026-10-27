from google import genai
import os
from dotenv import load_dotenv

#load .env file from parent directory
load_dotenv(r"C:\Code\gen-ai\.env")

API_KEY = os.getenv("GEMINI_API_KEY")

client  = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents ="Hi my name is Vibhor. I love to code in python. Write a short bio on me.",
)
print(response.text)

