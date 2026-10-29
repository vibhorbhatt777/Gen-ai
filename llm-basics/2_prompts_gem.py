from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv(r"C:\Code\gen-ai\.env")

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# uSER PROMPTS is the direct instruction or question you send to the ai model
#system prompts is the hidden instruction that set the behavior , tone and role of the AI.

# ia m sending the question to the llm = user promtp
user_prompt_1 = "Describe the F1 race in one sentence"

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents=user_prompt_1
)
print("without system prompt")
print(response.text)


# same with system prompts
user_prompt_2 = "Describe the F1 race in one sentence."

print("="*80)
print("System Prompt 1 : You are F1 race engineer.")
print("="*80)
response1 = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents=user_prompt_2,
    config=types.GenerateContentConfig(
        system_instruction="You are the F1 race engineer of the team red bull . tell me the engineer behind the F12 car . **Explain in easy way so that i understand each parts."

    )
)
print(response1.text)
print("/n")




